import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

#Gray 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# #BGR to HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# #BGR to lab
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

#RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# plt.imshow(rgb)
# plt.show()

#gray to bgr
bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('BGR', bgr)


cv.waitKey(0)