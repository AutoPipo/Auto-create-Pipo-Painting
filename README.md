# Easy Pipo
## "Pipo Painting" Auto Creation System
### Using Image Processing, the real image is automatically converted to a "Pipo Painting" canvas.   

<h3 align="center">Our Icon</h3>
<p align="center">
  <img src="/about_project/logo.png" width="25%" title="logo" ></img>
</p><br>

📌 **Name** : Easy Pipo     <br><br>
📌 **Authors** :  [Minku Koo](https://github.com/Minku-Koo) &nbsp;[Jiyong Park](https://github.com/Ji-yong219)      <br><br>
📌 **Development Period** : Feb.2021 ~ Jun.2021     <br><br>
📌 **Main Library** : [OpenCV](https://docs.opencv.org/master/), [numpy](https://numpy.org/doc/), [Flask](https://flask.palletsprojects.com/en/2.0.x/)     <br><br>
📌 **Keyword** : "Computer Vision", "Image Processing", "OpenCV", "Pipo Painting", "Line Detection", "Color Numbering"       <br><br>

## 📃 Table of Contents
- [Introduction](#pipo-painting-auto-creation-system)
- [What is Pipo Painting?](#-what-is-pipo-painting)    
- [How to Use?](#-how-to-use)    
- [Working Process](#-working-process)    
  * [Original Image](#original-image)     
  * [Step 1](#step-1-color-clustering-8-16-32-colors)    
  * [Step 2](#step-2-select-appropriate-number-of-colors-and-line-drawing)     
  * [Step 3](#step-3-remove-noise-line-and-set-color-numbering-color-label-included-or-not)     
- [Developed Modules](#-developed-modules)    
  + [Painting()](#-painting)
  + [DrawLine()](#-drawline)
  + [Numbering()](#-numbering)
- [Contact to us](#-contact-to-us)    

## 🤔 What is Pipo Painting?
<img src="/about_project/pipo-example.jpg" width="40%" title="pipopainting-example" style="float: left" ></img>    

#### "Pipo Painting" is also called "Paint by Number" or "Painting by Numbers".    

> It is a kit having a board on which light markings to indicate areas to paint, and each area has a number and a corresponding numbered paint to use. 
> The kits come with little compartmentalised boxes where the numbered colour pigments are stored. 
> The users are encouraged to wash the paintbrush every time a new numbered colour is being used.


[🔗 Wikipedia Discription](https://en.wikipedia.org/wiki/Paint_by_number)   
[🔗 Amazon Products](https://www.amazon.com/Pipo-Painting/s?k=Pipo+Painting)   
[🔗 Coupang Products](https://www.coupang.com/np/search?q=%ED%94%BC%ED%8F%AC%ED%8E%98%EC%9D%B8%ED%8C%85&channel=relate)     

## ⚙ How to Use?

#### Command Line
```
git clone https://github.com/AutoPipo/Auto-create-Pipo-Painting.git
cd Auto-create-Pipo-Painting
pip install -r requirements.txt
python .
```

#### On your Web Browser
```
https://localhost:5000
```

## 💡 Working Process

<h3  align="center">Original Image</h3>
<p align="center">
  <img src="/about_project/test-image/lala.jpg" width="50%" title="original"></img>
</p>

<h3 align="center" >Step 1. Color Clustering (8, 16, 32 Colors)</h3>
<!--<h3  align="center">8 Colors&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  16 Colors&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  32 Colors
</h3>-->
<p align="center">
  <img src="/about_project/test-image/lala-color-8.jpg" width="30%" title="8 colors" ></img>
  <img src="/about_project/test-image/lala-color-16.jpg" width="30%" title="16 colors"></img>
  <img src="/about_project/test-image/lala-color-32.jpg" width="30%" title="32 colors"></img>
</p>

<h3 align="center" >Step 2. Select appropriate number of colors and Line Drawing</h3>
<p align="center">
  <img src="/about_project/test-image/lala-lainedraw.jpg" width="50%" title="line drawing"></img>
</p>

<h3 align="center" >Step 3. Remove noise line and Set Color Numbering (Color Label Included or Not)</h3>
<!--<h3  align="center">Color Label Included&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Unincluded
</h3>-->
<p align="center">
  <img src="/about_project/test-image/lala-numbering-label.jpg" width="40%" title="numbering+label"></img>
  <img src="/about_project/test-image/lala-numbering.jpg" width="40%" title="numbering+non_label"></img>
</p>

<h3 align="center" >🔎 If it zoom in, you can see numbers</h3>
<p align="center">
  <img src="/about_project/test-image/lala-numbering-expand.jpg" width="50%" title="numbering-expand"></img>
</p>

## 📚 Developed Modules

### 📍 Painting()

> ***Painting()*** converts the image like a picture through reduce color.   
> Use Blurring and K-Means Clustering.   
> This is **step 1** of the [Working Steps](#-working-steps)     

```Python
    painting = Painting( "./imagePath/image.jpg")
    
    # Blurring
    blurImage = painting.blurring(  div = 8, 
                                    radius = 10, 
                                    sigmaColor =20, 
                                    medianValue=7)
    
    # Color K-Means Clustering
    clusteredImage = painting.colorClustering( blurImage, cluster = 16)
    
    expandedImage = imageExpand(clusteredImage, size = 4)
    
    # 확장된 이미지에서 변형된 색상을 군집화된 색상과 매칭
    similarMap = painting.expandImageColorMatch(expandedImage)
    # 군집화된 색상을 지정된 색상과 가장 비슷한 색상으로 매칭
    paintingMap = painting.getPaintingColorMap(similarMap)
```

### 📍 DrawLine()

> ***DrawLine()*** draw a line based on the color border.   
> Draw an arbitrary line at the edge of the image for apply Numbering()    
> This is **step 2** of the [Working Steps](#-working-steps)   

```Python
    drawLine = DrawLine(image)
    lineMap = drawLine.getDrawLine()
    outlines = drawLine.drawOutline(lineMap)
```

### 📍 Numbering()

> ***Numbering()*** input the color index number inside the line.     
> Find the contours and its hierarchy.    
> Extracts the color label, calculates the Incenter point, and input a color index number.     
> This is **step 3** of the [Working Steps](#-working-steps)    

```Python
    numbering = Numbering()
```

## 📧 Contact to us
- [Minku Koo](https://github.com/Minku-Koo) / corleone@kakao.com
- [Jiyong Park](https://github.com/Ji-yong219) / wldydslapjyy@naver.com 

