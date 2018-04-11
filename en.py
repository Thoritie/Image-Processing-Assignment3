from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt
from copy import deepcopy
import cv2


def getGrayColor(rgb):
    gray = int((int(rgb[0])+int(rgb[1])+int(rgb[2]))/3)
    return gray

def setRGB(r,g,b):
    r = int(r)
    g = int(g)
    b = int(b)
    return [r, g, b]

def brightImg(pixel, percent):
    pixel = int (pixel * percent + (1-percent) + pixel)
    return pixel

def darkImg(pixel, percent):
    pixel = int (pixel * percent + pixel)
    return pixel


img = Image.open('img/girl.jpg')
img = np.asarray(img)
# img = cv2.imread('img/girl.jpg')

colorImg = deepcopy(img)
# percentage = 50
percent = 0
percentage = int(input("Enter a percentage (%): "))
for i in range(len(img)):
        for j in range(len(img[i])):
            pixelR = int (img[i][j][0])
            pixelG = int (img[i][j][1])
            pixelB = int (img[i][j][2])

            if (percentage > 0):
                percent = percentage / 100
                r = brightImg(pixelR,percent)
                g = brightImg(pixelG,percent)
                b = brightImg(pixelB,percent)
            else:
                percent = percentage / 100
                r = darkImg(pixelR, percent)
                g = darkImg(pixelG, percent)
                b = darkImg(pixelB, percent)
            
            if (r > 255):
                r = 255
            if (g > 255):
                g = 255
            if (b > 255):
                b = 255
            
            colorImg[i][j] = setRGB(r,g,b)
      
 

       
plt.subplot(2,2,1)
plt.imshow(img)
plt.subplot(2,2,2)

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])

plt.subplot(2,2,3)
plt.imshow(colorImg)
plt.subplot(2,2,4)
# plt.hist(colorImg.ravel(),256,[0,256])
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([colorImg],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])

plt.show() 