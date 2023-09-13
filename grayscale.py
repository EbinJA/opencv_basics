import cv2 as cv
import numpy as np



vd = cv.VideoCapture('dog_video.mp4')

while vd.isOpened():
    ret, frame = vd.read()
    if ret == True:
        
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('dog video in b&w', frame)

        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

vd.release()
cv.destroyAllWindows()


