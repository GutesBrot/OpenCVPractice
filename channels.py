import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

b,g,r = cv.split(img)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

merged_b = cv.merge([b,blank,blank])
cv.imshow('Merged b', merged_b)

merged_g = cv.merge([blank,g,blank])
cv.imshow('Merged g', merged_g)

merged_r = cv.merge([blank,blank,r])
cv.imshow('Merged r', merged_r)

cv.waitKey(0)