import cv2 as cv

img= cv.imread('dog1.jpeg')#manipuation variable conv part
''' this img  is the manipulatable object
 all images and videos should be conv to a variable like img before processing '''


cv.imshow('dogimg',img)

cv.waitKey(0)