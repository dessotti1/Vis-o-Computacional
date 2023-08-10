import cv2 as cv

img = cv.imread("placa.PNG")

elem_estr = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))
imgE = cv.erode(img, elem_estr, iterations = 2)


elem_estr2 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (7, 7))
imgD = cv.dilate(img, elem_estr2, iterations = 2)

cv.imshow('Imagem 1', img)
cv.imshow('Imagem Erosão', imgE)
cv.imshow('Imagem Dilatação', imgD)

cv.waitKey(0)
cv.destroyAllWindows()
