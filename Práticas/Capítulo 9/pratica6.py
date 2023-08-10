import cv2 as cv
import numpy as np

img = cv.imread('washington.jpg', 1)

altura, largura, canais = img.shape
matriz = cv.getRotationMatrix2D((largura//2, altura//2), 180, 1)
imgRotacionada = cv.warpAffine(img, matriz, (largura, altura))

dx, dy = 40, 25
matriz = np.float32([[1, 0, dx], [0, 1, dy]])
imgDeslocada = cv.warpAffine(img, matriz,(largura, altura))

imgModificada = cv.resize(img, None, fx=0.5, fy=0.5, interpolation = cv.INTER_CUBIC)

cv.imshow("Imagem", img)
cv.imshow("Imagem Rotacionada", imgRotacionada)
cv.imshow("Imagem Transladada", imgDeslocada)
cv.imshow("Imagem Modificada", imgModificada)
cv.waitKey(0)
cv.destroyAllWindows()