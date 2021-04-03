﻿# color code

class HexColorCode:
    def __init__(self):
        self.hexColorCodes = """
FF8000,B45F04,61380B,DF7401,886A08,5F4C0B,B37126,AD6B20,
9B590D,72410A,86541B,765228,95652D,A86E2C,BC721E,9D5707,
A2551A,8C440D,663510,714625,A45C25,A7581C,A04C0B,9A4707,
600E08,661E19,551410,901F18,87332D,6A2E2A,951E16,550A05,80251F,A7271E,AF150A,
762B26,541814,53120E,530A05,161174,0D0872,17144D,0D0A43,25225D,120AA9,3C0807,
300808,460302,5D0705,4C1312,5F0D06,4C1510,430C07,41110C,
23214E,201C69,0C0A2F,201A97,
93DAFF,98DFFF,9DE4FF,A2E9FF,A7EEFF,
ACF3FF,B0F7FF,B4FBFF,B9FFFF,C0FFFF,
87CEFA,91D8FA,A5D8FA,AFDDFA,B9E2FA,
C3E7FA,CDECFA,D7F1FA,E1F6FA,EBFBFF,
00BFFF,0AC9FF,14D3FF,1EDDFF,28E7FF,
32F1FF,3CFBFF,46FFFF,96FFFF,C8FFFF,
00A5FF,00AFFF,00B9FF,00C3FF,00CDFF,
00D7FF,00E1FF,00EBFF,00F5FF,00FFFF,
1EA4FF,28AEFF,32B8FF,3CC2FF,46CCFF,
50D6FF,5AE0FF,6EE0FF,6EEAFF,78F3FF,
1E90FF,289AFF,32A4FF,3CAEFF,46B8FF,
50C2FF,5ACCFF,64D6FF,6EE0FF,78EAFF,
96A5FF,A0AFFF,AAB9FF,B4C3FF,BECDFF,
C8D7FF,D2E1FF,DCEBFF,E8F5FF,F4FFFF,
86A5FF,90AFFF,9AB9FF,A4C3FF,AECDFF,
B8D7FF,CCE1FF,E0EBFF,EBF5FF,F9FFFF,
6495ED,6E9FED,78A9ED,82B3ED,8CBDED,
96C7ED,A0D1F7,AADBFF,B4E5FF,BEEFFF,
0078FF,0A82FF,148CFF,1E96FF,28A0FF,
32AAFF,3CB4FF,46BEFF,50C8FF,5AD2FF,
0064FF,0A6EFF,1478FF,1E82FF,288CFF,
3296FF,3CA0FF,46AAFF,50B4FF,5ABEFF,
0000FF,3232FF,5050FF,646EFF,6478FF,
6482FF,648CFF,6496FF,64A0FF,64AAFF,
4169E1,4B73E1,557DE1,5F87E1,6991E1,
739BE1,7DA5E1,87AFEB,91B9F5,9BC3FF,
0064CD,0A6ECD,1478CD,1E82CD,288CD2,
3296D7,3CA0E1,46AAEB,50B4F5,5ABEF5,
5A5AFF,6464FF,6E6EFF,7878FF,8282FF,
8C8CFF,A0A0FF,B4B4FF,C8C8FF,D2D2FF,
7B68EE,8572EE,8F7CEE,9986EE,A390EE,
AD9AEE,B7A4EE,C1AEEE,CBB8EE,D5C2EE,
6A5ACD,7E6ECD,8878CD,9282CD,9C8CCD,
A696CD,B0A0CD,BAAAD7,C4B4E1,CEBEE1,
0000CD,2828CD,4646CD,6464CD,6E6ED7,
7878E1,8282EB,8C8CF5,9696FF,A0A0FF,
00008C,14148C,28288C,3C3C8C,50508C,
646496,7878AA,8C8CBE,A0A0C8,B4B4DC,
483D8B,52478B,5C518B,665B8B,70658B,
7A6F95,84799F,8E83A9,988DB3,A297BD,
000069,1E3269,323C73,3C467D,3C5087,
3C5A91,46649B,506EA5,5A78AF,6482B9,
3DFF92,47FF9C,51FFA6,5BFFB0,65FFBA,
6FFFC4,79FFCE,75FFCA,7AFFCF,7FFFD4,
55EE94,5FEE9E,69EEA8,73EEB2,7DEEBC,
87EEC6,91F8D0,9BFFDA,A5FFE4,AFFFEE,
66CDAA,70D2B4,7AD7BE,84DCC8,8EE1D2,
98EBDC,9DF0E1,A2F5E6,A7FAEB,ACFFEF,
AAEBAA,B4F0B4,BEF5BE,C8FAC8,D2FFD2,
DCFFDC,E1FFE1,E6FFE6,EBFFEB,F0FFF0,
80E12A,8AE634,94EB3E,9EF048,A8F552,
B2FA5C,BCFF66,C1FF6B,C6FF70,CBFF75,
52E252,5CE75C,66EC66,70F170,7AF67A,
84FB84,89FB89,8EFB8E,93FB93,98FB98,
64CD3C,6ED746,78E150,82EB5A,8CF064,
96F56E,9BFA73,A0FA78,A5FA7D,AAFA82,
13C7A3,18CCA8,1DD1AD,22D6B2,27DBB7,
2CE0BC,31E0C1,36E0C6,3BE0CB,40E0D0,
46B4B4,50BEBE,5AC8C8,64D2D2,6EDCDC,
73E1E1,78E6E6,7DEBEB,82F0F0,87F5F5,
20B2AA,2ABCB4,34C6BE,3ED0C8,48DAD2,
52E4DC,57E9E1,5CEEE6,61F3EB,66F8F0,
5F9EA0,69A8AA,73B2B4,7DBCBE,87C6C8,
91D0D2,96D5D7,9BDADC,A0DFE1,A5E3E6,
3CB371,46BD7B,50C785,5AD18F,64DB99,
6EE5A3,73EAA8,78EFAD,7DF4B2,82F9B7,
2E8B57,389561,429F6B,4CA975,56B37F,
60BD89,65C28E,6AC793,6FCC98,74D19D,
228B22,2C952C,369F36,40A940,4AB34A,
54BD54,5EC75E,63CC63,68D168,6DD66D,
497649,538053,5D8A5D,679467,719E71,
7BA87B,80AD80,85B285,8AB78A,8FBC8F,
006400,0A6E0A,147814,1E821E,288C28,
329632,3CA03C,41A541,46AA46,4BAF4B,
008C8C,0A9696,14A0A0,1EAAAA,28B4B4,
32BEBE,37C3C3,3CC8C8,41CDCD,46D2D2,
008080,0A8A8A,149494,1E9E9E,28A8A8,
32B2B2,37B7B7,3CBCBC,41C1C1,46C6C6,
FFB6C1,FFBBC6,FFC0CB,FFC5D0,FFCAD5,
FFCFDA,FFD4DF,FFD9E4,FFDEE9,FFE3EE,
FFAAAF,FFB4B9,FFBEC3,FFC8CD,FFD2D7,
FFDCE1,FFE1E6,FFE6EB,FFEBF0,FFF0F5,
FF9E9B,FFA8A5,FFB2AF,FFBCB9,FFC6C3,
FFD0CD,FFD5D2,FFDAD7,FFDFDC,FFE4E1,
FF7A85,FF848F,FF8E99,FF98A3,FFA2AD,
FFACB7,FFB1BC,FFB6C1,FFBBC6,FFC0CB,
FF5675,FF607F,FF6A89,FF7493,FF7E9D,
FF88A7,FF92B1,FF9CBB,FFA6C5,FFB0CF,
FF82FF,FF8CFF,FF96FF,FFA0FF,FFAAFF,
FFB4FF,FFBEFF,FFC8FF,FFD2FF,FFDCFF,
FF7DB4,FF87BE,FF91C8,FF9BD2,FFA5DC,
FFAFE6,FFB4EB,FFB9F0,FFBEF5,FFC3FA,
FF69B4,FF73BE,FF7DC8,FF87D2,FF91DC,
FF9BE6,FFA5F0,FFAAF5,FFAFFA,FFB4FF,
FF1493,FF1E9D,FF28A7,FF32B1,FF3CBB,
FF46C5,FF50CF,FF5AD9,FF64E3,FF6EED,
DB7093,DB7A9D,DB84A7,E08EB1,E598BB,
EAA2C5,EAB1D4,EFACCF,F4BBDE,F4B6D9,
D7567F,DC6089,E16A93,E6749D,EB7EA7,
F088B1,F592BB,FA9CC5,FFA6CF,FFB0D9,
C71585,C71F8F,C73399,C73DA3,CC47AD,
D151B7,D65BC1,E065CB,EA6FD5,F479DF,
CD1039,CD1F48,CD2E57,CD3861,CD426B,
D24C75,D7567F,DC6089,E16A93,E6749D,
B9062F,B91A4D,BE2457,C32E61,C8386B,
CD4275,D24C7F,D75689,DC6093,E16A9D,
FAEB78,FAF082,FAF58C,FAFA96,FAFAA0,
FAFAAA,FAFAB4,FAFABE,FAFAD2,FAFAD2,
FFDC3C,FFE146,FFE650,FFEB5A,FFF064,
FFF56E,FFFA78,FFFA82,FFFF8C,FFFF96,
FFC81E,FFD228,FFD732,FFDC3C,FFE146,
FFE650,FFEB5A,FFF064,FFF56E,FFF978,
FFB400,FFBE0A,FFC314,FFC81E,FFCD28,
FFD232,FFD73C,FFDC46,FFE150,FFE65A,
FDCD8C,FDD296,FDD7A0,FDDCAA,FDE1B4,
FDE6BE,FDEBC8,FDF5D2,FDF5DC,FDF5E6,
FAC87D,FACD87,FAD291,FAD79B,FADCA5,
FAE1AF,FAE6B9,FAEBC3,FAEBCD,FAEBD7,
FFA500,FFAF0A,FFB914,FFC31E,FFCD28,
FFD732,FFDC37,FFE13C,FFE641,FFEB46,
FF9100,FF9B00,FFA500,FFAF00,FFB900,
FFC300,FFC800,FFCD00,FFD200,FFD700,
FF8200,FF8C0A,FF9614,FFA01E,FFAA28,
FFB432,FFB937,FFBE3C,FFC341,FFC846,
FFA98F,FFB399,FFBDA3,FFC7AD,FFD1B7,
FFDBC1,FFE0C6,FFE5CB,FFEAD0,FFEFD5,
FFA374,FFAD7E,FFB788,FFC192,FFCB9C,
FFD0A1,FFD5A6,FFDAAB,FFDFB0,FFE4B5,
FF9473,FF9E7D,FFA887,FFB291,FFBC9B,
FFC6A5,FFD0AF,FFD0AF,FFD5B4,FFDAB9,
FF7F50,FF895A,FF9364,FF9D6E,FFA778,
FFB182,FFBB8C,FFC091,FFC596,FFCA9B,
CD853F,CD8F49,D29953,D7A35D,DCAD67,
E1B771,E6C17B,EBC680,F0CB85,F5D08A,
D2691E,D27328,D27D32,D7873C,DC9146,
E19B50,E6A55A,EBAA5F,EBAF64,F0B469,
AE5E1A,B86824,C2722E,CC7C38,D68642,
E0904C,E59551,EA9A56,EF9F5B,F4A460,
8B4513,8B4F1D,8B5927,8B6331,906D3B,
957745,9F814F,A48654,A98B59,AE905E,
FF9696,FFA0A0,FFAAAA,FFB4B4,FFBEBE,
FFC8C8,FFD2D2,FFDCDC,FFE6E6,FFF0F0,
F08080,F08A8A,F09494,F59E9E,FAA8A8,
FAB2B2,FAB7B7,FABCBC,FAC1C1,FAC6C6,
F56E6E,F57878,F58282,F58C8C,F59696,
F5A0A0,F5AAAA,FAB4B4,FABEBE,FAC8C8,
F06464,F06E6E,F07878,F08282,F08C8C,
F09696,F4A0A0,F4AAAA,F4B4B4,FEBEBE,
FF0000,FF3232,FF4646,FF5050,FF5A5A,
FF6464,FF6E6E,FF7878,FF8282,FF8C8C,
EB0000,EB3232,EB4646,EB5050,EB5A5A,
EB6464,F06E6E,F57878,FA8282,FA8C8C,
CD0000,CD3C3C,CD4646,CD5050,D25A5A,
D76464,DC6E6E,E17878,E68282,EB8C8C,
CD5C5C,CD6666,CD7070,CD7A7A,D28484,
D78E8E,DC9898,E6A2A2,EBACAC,F0B6B6,
B90000,B93232,B93C3C,B94646,B95050,
BE5A5A,C35F5F,C86464,CD6969,D26E6E,
B22222,B24040,B24A4A,B25454,B75E5E,
BC6868,C17272,CB7776,CB7C7C,D08180,
A52A2A,AA3E3E,AF4848,B45252,BE5C5C,
C36666,CD7070,CD7A7A,D28484,D78E8E,
800000,803232,853C3C,8F4646,945050,
9E5A5A,A36464,AD6E6E,B77878,C18282,
CD853F,CD8B45,CD904A,D2954F,D29A54,
D79F59,D7A45E,E1A963,E1AE68,E6B36D,
DB631F,E56D29,E57733,EA813D,EF8B47,
EF904C,F49551,F49A56,F49F5B,F4A460,
D2691E,D27328,D77D32,D7873C,DC9146,
E19B50,E6A055,EBA55A,F0AA5F,F5AF64,
A0522D,A05C37,A06641,A5704B,AA7A55,
B4845F,B98E69,C39873,CDA27D,D7AC87,
8B4513,8B4F1D,8B5927,8B6331,906D3B,
9A7745,A4814F,AE8B59,B89563,C29F6D,
DA70D6,DF75DB,E47AE0,E97FE5,EE84EA,
F389EF,F88EF4,FD93F9,FF98FE,FF9DFF,
BA55D3,BF5AD8,C45FDD,C964E2,CE69E7,
D36EEC,D873F1,DD78F6,E27DFB,E782FF,
9932CC,9E37D1,A33CD6,A841DB,AD46E0,
B24BE5,B750EA,BC55EF,C15AF4,C65FF9,
9400D3,9905D8,9E0ADD,A30FE2,A814E7,
AD19EC,B21EF1,B723F6,BC28FB,C12DFF,
942894,9E329E,A83CA8,B246B2,BC50BC,
C65AC6,D064D0,DA6EDA,E478E4,EE82EE,
8C008C,960A96,A014A0,AA1EAA,B428B4,
BE32BE,C83CC8,D246D2,DC50DC,E65AE6,
800080,8A0A8A,941494,9E1E9E,A828A8,
B232B2,BC3CBC,C646C6,D050D0,DA5ADA,
834683,8D508D,975A97,A164A1,AB6EAB,
B578B5,BF82BF,C98CC9,D396D3,DDA0DD,
828282,8C8C8C,969696,A0A0A0,AAAAAA,
B4B4B4,BEBEBE,C8C8C8,D2D2D2,DCDCDC,
000000,282828,323232,3C3C3C,464646,
505050,5A5A5A,646464,6E6E6E,787878
"""
        self.hexColorCode = """
FF0000,00FF00,0000FF,
CD5C5C,7FFFD4,
00FFFF,E9967A,00FA9A,
00FFFF,F08080,
00FF7F,48D1CC,FA8072,
98FB98,00CED1,
FF4500,ADFF2F,5F9EA0,
DC143C,7FFF00,
708090,B22222,7CFC00,
E0FFFF,8B0000,
008000,AFEEEE,C71585,
90EE90,B0E0E6,
FFC0CB,9ACD32,B0C4DE,
FFB6C1,32CD32,
4682B4,FF69B4,3CB371,
ADD8E6,FF1493,
8FBC8F,87CEEB,DB7093,
228B22,87CEFA,
BDB76B,2E8B57,00BFFF,
F0E68C,6B8E23,
6495ED,EEE8AA,808000,
4169E1,FAFAD2,
556B2F,7B68EE,FFFFE0,
006400,1E90FF,
FFFACD,66CDAA,0000CD,
FFFF00,40E0D0,
00008B,FFD700,20B2AA,
000080,FFEFD5,
008B8B,191970,FFE4B5,
008080,DCDCDC,
FFDAB9,F0FFF0,D3D3D3,
FFA07A,F5FFFA,
C0C0C0,FFA500,F0FFFF,
A9A9A9,FF8C00,
F0F8FF,808080,FF7F50,
F8F8FF,696969,
FF6347,F5F5F5,2F4F4F,
FF4500,FFF0F5,
778899,E6E6FA,FFE4E1,
CD853F,D8BFD8,
FAEBD7,D2691E,DDA0DD,
FFF5EE,800000,
EE82EE,FFFAFA,8B4513,
FF00FF,F5F5DC,
A52A2A,FF00FF,FAF0E6,
A0522D,DA70D6,
FDF5E6,8B0000,FFF8DC,
FFFAF0,DEB887,
FFEBCD,FFFFF0,D2B48C,
FFE4E4,BA55D3,
BC8F8F,FFDEAD,9932CC,
9370DB,8A2BE2,
9400D3,8B008B,6A5ACD,
800080,F5DEB3,
483D8B,4B0082,B8860B,
F4A460,DAA520,
000000,FFFFFF,
472B09,683B04,432F16,65441C,492902,5D3A0F,
076C0E,104913,17731D,1F6724,24782A,06B912,1E6723,
0E0F58,06086D,040695,090A56,1A1A42,14154B,
610B0B,8A0808,B40404,3B170B,61210B,3B240B,61380B,
3B240B,61380B,0B173B,0B2161,3B0B17,610B21,2E2E2E,0B3B17,0B6138,
0B610B,0B3B0B,0B0B3B,0B0B61,0B173B,0B2161,3B0B0B
"""
        
        self.hexColorCodeList = self.hexColorCode.replace("\n", "").split(",")
        
if __name__ == "__main__":
    code = HexColorCode().hexColorCodeList
    print(len(code))
            
            
            
            
            
            
            
            
            
            
        
        