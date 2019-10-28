from PIL import Image, ImageFilter #pip install pillow
import numpy as np
from PegarDados import pickImage
import os
import math

#onde pegar os links https://pt-br.topographic-map.com/
cores = [(255, 255, 255), #1579m
(255, 197, 197), #1517
(255, 140, 140), #1457
(255, 82, 82), #1398
(255, 25, 25),  #1340
(255, 32, 0), #1284
(255, 89, 0), #1230
(255, 147, 0), #1178
(255, 204, 0), #1128
(249, 255, 0), #1079
(192, 255, 0), #1033
(134, 255, 0), #989
(76, 255, 0), #947
(19, 255, 0), #908
(0, 255, 75), #871
(0, 255, 191), #837
(0, 230, 255), #806
(0, 173, 255), #778
(0, 115, 255), #755
(0, 58, 255),#737
(0, 0, 255)] #728
alturas = [1579,1517,1457,1398,1340,1284,1230,1178,1128,1079,1033,989,947,908,871,837,806,778,755,737,728]

url = "https://pt-br.topographic-map.com/maps/g5zv/Brumadinho/"
def passo1(url= ''):
    if os.path.isfile("./imagens/"+(url.split('/')[5])+".png"):
        img = Image.open("./imagens/"+(url.split('/')[5])+".png")
        img.show()
    else: 
        img = Image.open("./imagens/"+pickImage.pegarImage(link= url))

    #img.show()
    # img_sharp = img.filter(ImageFilter.SHARPEN) ##filtro na imagem
    # img_sharp.save('imagens/Brumadinho_sharpened.jpg','JPEG')
    # r,g,b = img_sharp.split() #separar em rgb

    if os.path.isfile("./imagens/"+(url.split('/')[5])+"_distance.png"):
        img = Image.open("./imagens/"+(url.split('/')[5])+"_distance.png")
        img.show()
    else: 
        size = width,height = img.size;
        matriz = []
        mat1 = []
        coordenada = 10,10
        try:
            for x in range(0,width):
                for y in range(0,height):
                    coordenada = x,y
                    if img.getpixel(coordenada) not in cores:
                        (r,g,b) = img.getpixel(coordenada)
                        dist = []
                        for cor in cores:
                            for cor in cores: 
                                dist.append(distanciaRGB((r,g,b),(cor)))
                        img.putpixel(coordenada, cores[dist.index(min(dist))])
                        mat1.append(alturas[dist.index(min(dist))])
                matriz.append(mat1)
                mat1 = []
        except IndexError:
            print("Erro de out of range")
        print(len(matriz),size)
        arq = open("./matriz/"+(url.split('/')[5])+".txt","w")
        arq.write(str(matriz))
        arq.close()
        img.show()
        img.save("./imagens/"+(url.split('/')[5])+"_distance.png")

def distanciaRGB(rgb1,rgb2):
    r1,g1,b1 = rgb1
    r2,g2,b2 = rgb2
    d1 = math.sqrt(math.pow(r1-r2,2)+math.pow(g1-g2,2)+math.pow(b1-b2,2))
    return d1


passo1(url)