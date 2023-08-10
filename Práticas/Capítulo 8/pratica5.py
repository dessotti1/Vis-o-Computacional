import cv2 as cv
import numpy as np

largura, altura = 600, 400
bandeira = np.zeros((altura, largura, 3), dtype= np.uint8)

verde = (0, 128, 0)
cv.rectangle(bandeira, (0, 0), (largura, altura), verde, -1)

amarelo = (0, 255, 255)
pontos = np.array([[50, altura//2], [largura//2, 350], [550, altura//2], [largura//2, 50]])
cv.fillConvexPoly(bandeira, pontos, amarelo)

azul = (255, 0, 0)
cv.circle(bandeira, (largura//2, altura//2), 80, azul, -1)

cv.imshow("Bandeira do Brasil", bandeira)
cv.waitKey(0)
cv.destroyAllWindows()