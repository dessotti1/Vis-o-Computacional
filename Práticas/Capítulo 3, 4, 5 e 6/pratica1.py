import cv2 as cv

img = cv.imread('pratica1.png', 1)

altura, largura, canais = img.shape
tipo = img.dtype

img_cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imwrite('pratica1_cinza.png', img_cinza)

print(altura)
print(largura)
print(canais)
print(tipo)


cv.imshow('Imagem', img)
cv.imshow('Imagem em Cinza', img_cinza)
cv.waitKey(0)
cv.destroyAllWindows()

