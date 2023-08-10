import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print('Erro!')
    exit()

while True:
    ret, frame = cap.read()
    if ret == True:

        largura, altura = frame.shape
        cv.ellipse(frame, (largura//2, altura//2), (100, 150), 0, 0, 360, (0, 0, 255), 3)
        cv.imshow('WebCam', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break