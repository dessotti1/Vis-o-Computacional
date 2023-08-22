import cv2 as cv
import numpy as np

img = cv.imread('triangulo.JPG', 0)

ret, imgBin = cv.threshold(img, 0, 255, cv.THRESH_BINARY_INV)

contours, _ = cv.findContours(imgBin, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

if len(contours) > 0:

    obj = contours[0]
    area = cv.contourArea(obj)
    perimetro = cv.arcLength(obj, True)

    print(area)
    print(perimetro)

else:
    print("Sem objeto detectado.")
