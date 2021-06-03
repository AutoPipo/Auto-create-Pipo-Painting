﻿# flask server
# Author : minku Koo
# Project Start:: 2021.03.10
# Last Modified from Ji-yong 2021.03.30

from flask import Flask, request, render_template, jsonify, Blueprint, redirect, url_for, session, current_app
import cv2
# import matplotlib.pyplot as plt
import numpy as np
# import sqlite3 as sqlite
# import json
import os
# from libs.brush import Brush
from libs.utils import *
from libs.imageProcessing import *
from libs.drawLine import *
from libs.painting import *

from multiprocessing import Process, Queue, Manager

import logging

views = Blueprint("server", __name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@views.route("/", methods=["GET"])
def index():
    if "id" not in session:
        session["id"] = get_job_id()
    
    # session.pop("id")
    return render_template("index.html")
    
@views.route("/howToUse", methods=["GET"])
def howToUse():
    if "id" not in session:
        session["id"] = get_job_id()
    
    return render_template("how_to_use.html")
    
@views.route("/whatIsPipo", methods=["GET"])
def whatIsPipo():
    if "id" not in session:
        session["id"] = get_job_id()
    
    return render_template("what_is_pipo.html")
    
@views.route("/ColorSetting", methods=["GET"])
def ColorSetting():
    if "id" not in session:
        session["id"] = get_job_id()
    
    return render_template("color_setting.html")

@views.route("/uploadIMG", methods=["POST"])
def upload_img():
    if 'file' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp

    files = request.files.getlist('file')

    errors = {}
    success = False
    filepath = None

    for file in files:
        if file:
            # filename = secure_filename(file.filename) # secure_filename은 한글명을 지원하지 않음
            filename = file.filename 
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file_page_path = os.path.splitext(filepath)[0]
            
            # pdf file save (with uploaded)
            file.save(filepath)
            success = True

        else:
            errors[file.filename] = 'File type is not allowed'
    
    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 206
        return resp

    # main 
    if success:
        resp = jsonify({'message' : 'Files successfully uploaded'})
        resp.status_code = 201
        return resp

    else:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp


colorNames = {}
colors = {}

def reduce_color_process(idx, image_path, img, cluster, result):
    global colorNames
    global colors

    paintingTool = Painting(image_path)

    print(f'{idx}번 프로세스 컬러 군집화 시작')
    clusteredImage = paintingTool.colorClustering( img, cluster = cluster )
    
    print(f'{idx}번 프로세스 이미지 확장')
    expandedImage = imageExpand(clusteredImage, guessSize = True)
    
    print(f'{idx}번 프로세스 컬러 매칭 시작')
    paintingMap = paintingTool.expandImageColorMatch(expandedImage)

    print(f'{idx}번 프로세스 컬러 추출 시작')
    colorNames_, colors_ = getColorFromImage(paintingMap)

    print(f'{idx}번 프로세스 컬러 {len(colorNames_)}개')

    colorNames[cluster] = colorNames_
    colors[cluster] = colors_

    result.put(paintingMap)

    return


@views.route("/convert", methods=["POST"])
def convert():
    global colorNames
    global colors

    global img_lab
    global labs
    global painting_map


    job = request.form['job']
    image_path = request.form['image_path']
    
    image_path = './web'+image_path[2:]
    image_name = os.path.basename(image_path)
    
    paintingTool = Painting(image_path)

    if job == "start":
        image = paintingTool.image

        image_name2 = image_name.split('.')[0]+"_origin." + image_name.split('.')[1]
        cv2.imwrite(f'./web/static/render_image/{image_name}', image)
        cv2.imwrite(f'./web/static/render_image/{image_name2}', image)
        return jsonify(target="#original_img", img_name=image_name2)

    elif job == "reduce_color":
        paintingTool.image = cv2.imread(f'./web/static/render_image/{image_name}')
        image = paintingTool.image

        print(f'블러 시작')

        # 색 단순화 + 블러 처리
        blurImage = paintingTool.blurring(
            div = 8, 
            radius = 10, 
            sigmaColor =20, 
            medianValue=7
        )

        manager = Manager()
        result_list = manager.Queue()
        clusters = [16, 24, 32]
        processes = []

        for idx, cluster in enumerate(clusters):
            process = Process(target=reduce_color_process, args=(idx+1, image_path, blurImage, cluster, result_list))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        painting_map_16 = result_list.get()
        painting_map_24 = result_list.get()
        painting_map_32 = result_list.get()


        image_name2 = image_name.split('.')[0]+"_reduce." + image_name.split('.')[1]
        image_name2_16 = image_name.split('.')[0]+"_reduce_16." + image_name.split('.')[1]
        image_name2_24 = image_name.split('.')[0]+"_reduce_24." + image_name.split('.')[1]
        image_name2_32 = image_name.split('.')[0]+"_reduce_32." + image_name.split('.')[1]
        
        cv2.imwrite(f'./web/static/render_image/{image_name2_16}', painting_map_16)
        cv2.imwrite(f'./web/static/render_image/{image_name2_24}', painting_map_24)
        cv2.imwrite(f'./web/static/render_image/{image_name2_32}', painting_map_32)

        return jsonify(target="#reduce_img", img_name=image_name2)

    elif job == "draw_line":
        image_name2 = image_name.split('.')[0]+"_reduce." + image_name.split('.')[1]
        paintingTool.image = cv2.imread(f'./web/static/render_image/{image_name2}')
        paintingMap = paintingTool.image


        # 선 그리기
        print(f'선 그리기 시작')
        drawLineTool = DrawLine(paintingMap)
        lined_image = drawLineTool.getDrawLine()
        lined_image = drawLineTool.drawOutline(lined_image)

        # 레이블 추출
        img_lab, lab = getImgLabelFromImage(colors, paintingMap)


        image_name2 = image_name.split('.')[0]+"_linedraw." + image_name.split('.')[1]
        cv2.imwrite(f'./web/static/render_image/{image_name2}', lined_image)


        # lined_image = cv2.convertScaleAbs(lined_image)
        return jsonify(target="#linedraw_img", img_name=image_name2)

    elif job == "numbering":
        image_name2 = image_name.split('.')[0]+"_reduce." + image_name.split('.')[1]
        paintingTool.image = cv2.imread(f'./web/static/render_image/{image_name2}')
        lined_image = paintingTool.image



        # contour, hierarchy 추출
        print(f'컨투어 추출 시작')
        contours, hierarchy, thresh = getContoursFromImage(lined_image.copy())


        # 결과 이미지 백지화
        result_img = makeWhiteFromImage(lined_image)
        # result_img = paintingMap

        # 결과이미지 렌더링
        # image를 넣으면 원본이미지에 그려주고, result_img에 넣으면 백지에 그려줌
        print(f'넘버링 시작')
        result_img = setColorNumberFromContours2(result_img, thresh, contours, hierarchy, img_lab, lab, colorNames)

        print(f'컬러 레이블링 시작')
        result_img = setColorLabel(result_img, colorNames, colors)

        print(f'작업 완료')

        image_name2 = image_name.split('.')[0]+"_numbering." + image_name.split('.')[1]
        cv2.imwrite(f'./web/static/render_image/{image_name2}', result_img)
        return jsonify(target="#numbering_img", img_name=image_name2)

    return jsonify(img_name=image_name)