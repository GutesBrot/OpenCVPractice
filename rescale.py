import cv2 as cv

def rescaleFrame(frame, scale=0.75): 
    #Images, Video, live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    #live video
    capture.set(3, width)
    capture.set(4, height)

#Video Read
capture = cv.VideoCapture('Videos/cat.mp4')

while True: 
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, 0.25)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()