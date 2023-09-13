import cv2 as cv
import numpy as np

vd=cv.VideoCapture('dog_video.mp4')



x,y,w,h= 700, 120, 200, 200



while vd.isOpened():
    ret,frame=vd.read()
    if ret == True:
        roi=frame[y:y+h,x:x+w]
        blurred_reg=cv.GaussianBlur(roi,(81,81),0)
        frame[y:y+h,x:x+w]=blurred_reg
        cv.imshow('blurred part video',frame)
        #cv.imshow('dog video',frame)

        if cv.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break


vd.release()

cv.destroyAllWindows()




