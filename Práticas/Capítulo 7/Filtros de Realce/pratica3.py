import cv2 as cv

img = cv.imread('taj.jpg', 1)

sobelx = cv.Sobel(img,cv.CV_64F, 1, 0,ksize=3)
sobely = cv.Sobel(img,cv.CV_64F, 0, 1,ksize=3)

img_laplaciano = cv.Laplacian(img, cv.CV_8U)

img_canny = cv.Canny(img, 125, 200)

cv.imshow('Imagem 1', img)
cv.imshow('Imagem Sobel X', sobelx)
cv.imshow('Imagem Sobel Y', sobely)
cv.imshow('Imagem Laplaciano', img_laplaciano)
cv.imshow('Imagem Canny', img_canny)

cv.waitKey(0)
cv.destroyAllWindows()
