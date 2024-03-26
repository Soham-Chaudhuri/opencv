import cv2 as cv
import numpy as np
img=cv.imread('data\lena.jpg')

lr1=cv.pyrDown(img)
lr2=cv.pyrDown(lr1)
ur1=cv.pyrUp(lr2)
lp=cv.subtract(lr1,ur1)

cv.imshow('image',img)
# cv.imshow('1',lr1)
# cv.imshow('2',lr2)
# cv.imshow('3',ur1)
cv.imshow('Laplacian',lp)
cv.waitKey(0)
cv.destroyAllWindows()


#Laplacian pyramid- Diff b/w the gaussian level A and A-1
#Blend and recontruct the images- uses