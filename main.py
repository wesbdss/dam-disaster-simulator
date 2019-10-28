from PIL import Image, ImageFilter #pip install pillow
import numpy as np
from PegarDados import pickImage

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


img = Image.open("imagens/"+pickImage.pegarImage(link= "https://pt-br.topographic-map.com/maps/g5zv/Brumadinho/"))
img.show()
# img_sharp = img.filter(ImageFilter.SHARPEN) ##filtro na imagem
# img_sharp.save('imagens/Brumadinho_sharpened.jpg','JPEG')
# r,g,b = img_sharp.split() #separar em rgb
size = width,height = img.size;
#print(size)
coordenada = 10,10
print(img.getpixel(coordenada))
img.paste("blue",(0,0,20,20))
img.show()


# print(list(img.getdata()))