import cv2 as cv
import numpy as np

vd=cv.VideoCapture('dog_video.mp4')


while vd.isOpened():
    ret,frame=vd.read()
    if ret == True:
        cv.imshow('dog video',frame)

        if cv.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

vd.release()

cv.destroyAllWindows()




