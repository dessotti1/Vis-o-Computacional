import cv2 as cv

img = cv.imread('washington.jpg')

B, G, R, alpha = cv.mean(img)

print(B)
print(G)
print(R)
print(alpha)

mean, stdDev = cv.meanStdDev(img)

print(mean)
print(stdDev)