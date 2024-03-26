import numpy as np
import cv2 as cv

img=cv.imread('data\Baseball_(crop).jpg',1)
imgray=cv.imread('data\Baseball_(crop).jpg',0)
ret,thresh=cv.threshold(imgray,127,255,0)
contours,hierarchy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
cv.drawContours(img,contours,-1,(0,255,0),3)
cv.imshow('Image',img)
cv.imshow('Image Gray',imgray)
cv.waitKey(0)
cv.destroyAllWindows()