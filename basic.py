import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

#Greyscale
gray =  cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Blur 
blurred = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blurred)

#Edge Cascade
canny =  cv.Canny(blurred, 125, 175)
cv.imshow('Canny', canny)

# Dilating the image 
dilated = cv.dilate(canny, (7,7), iterations=1)
cv.imshow('Dilated', dilated)

# Eroding 
eroded = cv.erode(dilated,(7,7), iterations= 1)
cv.imshow('Eroded', eroded)

#Resize 
resize = cv.resize(img, (500,500), interpolation= cv.INTER_CUBIC) # apparently INTER_CUBIC is the slowest but best
cv.imshow('Resized', resize)

# Crop 
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)