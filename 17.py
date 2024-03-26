import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('data\sudoku.png',0)
_,th1=cv.threshold(img,127,255,cv.THRESH_BINARY)
th2=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,9,10)
th3=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,15,10)
cv.imshow('sudoku',img)
cv.imshow('th1',th1)
cv.imshow('th2',th2)
cv.imshow('th3',th3)

cv.waitKey(0)
cv.destroyAllWindows()
