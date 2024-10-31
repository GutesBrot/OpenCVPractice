import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype= 'uint8')
cv.imshow('Blank', blank)

#Paint image a color
# blank[:] = 0,0,255
# cv.imshow('Green', blank)

#Draw a rectangle
# cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=2)
# cv.imshow('Rectangle', blank)

#Draw a circle 
# cv.circle(blank, center=(blank.shape[1]//2,blank.shape[0]//2),color=(0,255,0), radius= 30)
# cv.imshow('Circle', blank)

#Draw a line 
cv.line(blank, (0,0), (blank.shape[1], blank.shape[0]), (0,255,0), 2)

cv.imshow('Line', blank)

cv.waitKey(0)