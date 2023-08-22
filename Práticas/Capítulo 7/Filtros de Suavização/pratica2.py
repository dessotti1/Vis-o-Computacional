import cv2 as cv
import numpy as np

img1 = cv.imread('kennedy.jpg', 1)
img_media = cv.blur(img1, (9,9))

img2 = cv.imread('gaussiano.jpg', 1)
img_gaussiano = cv.GaussianBlur(img2, (7, 7), 0)

img3 = cv.imread('sal.png', 1)
img_mediana = cv.medianBlur(img3, 5)


cv.imshow('Imagem 1', img1)
cv.imshow('Imagem 2', img2)
cv.imshow('Imagem 3', img3)


cv.imshow('Imagem Média', img_media)
cv.imshow('Imagem sem ruído gaussiano', img_gaussiano)
cv.imshow('Imagem sem ruído sal e pimenta', img_mediana)

cv.waitKey(0)
cv.destroyAllWindows()

