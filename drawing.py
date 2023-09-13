import cv2 as cv
import numpy as np

cap=cv.imread('park.jpg')

cv.imshow('drawimg',cap)

#converting to grayscale

gray=cv.cvtColor(cap,cv.COLOR_BGR2GRAY)

cv.imshow('bandw',gray)

#blurring



cv.waitKey(0)