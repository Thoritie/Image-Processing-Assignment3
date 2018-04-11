from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt
from copy import deepcopy
import cv2

#set color
color = [[0, 0, 102],[153, 204, 255],[255, 153, 208],[255, 229, 204],[153, 0, 0],[255, 255, 0]]
# blue = [0, 0, 102]
# light = [153, 204, 255]
# pink = [255, 153, 208]
# cream = [255, 229, 204]
# red = [153, 0, 0]
# yellow = [255, 255, 0]

def getGrayColor(rgb):
    gray = int((int(rgb[0])+int(rgb[1])+int(rgb[2]))/3)
    return gray

    

img = Image.open('img/mri.jpg')
img = np.asarray(img)

colorImg = deepcopy(img)

# for c in range(0,3):
#     c = int(input("Enter a range: "))
#     name = int(input("Enter a name no. : "))
#     for i in range(len(img)):
#         for j in range(len(img[i])):
#             pixel = getGrayColor(img[i][j])
#             if pixel > c:
#                 colorImg[i][j] = color[name]

c1 = int(input("Enter a range: blue"))
c2 = int(input("Enter a range: light"))
c3 = int(input("Enter a range: pink"))
c4 = int(input("Enter a range: cream"))
c5 = int(input("Enter a range: red"))
c6 = int(input("Enter a range: yellow"))

for i in range(len(img)):
        for j in range(len(img[i])):
            pixel = getGrayColor(img[i][j])
            if pixel >= c1:
                colorImg[i][j] = color[0]
            elif pixel >= c2:
                colorImg[i][j] = color[1]
            elif pixel >= c3:
                colorImg[i][j] = color[2]
            elif pixel >= c4:
                colorImg[i][j] = color[3]
            elif pixel >= c5:
                colorImg[i][j] = color[4]
            elif pixel >= c6:
                colorImg[i][j] = color[5]
            else:
                colorImg[i][j] = color[5]
            

        
plt.subplot(2,2,1)
plt.imshow(img)
plt.subplot(2,2,2)
plt.hist(img.ravel(),256,[0,256])
plt.subplot(2,2,3)
plt.imshow(colorImg)
plt.subplot(2,2,4)
plt.hist(colorImg.ravel(),256,[0,256])


plt.show() 
