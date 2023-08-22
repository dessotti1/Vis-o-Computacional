import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print('Erro!')
    exit()

while True:
    ret, frame = cap.read()
    if ret == True:

        cv.imshow('WebCam', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break