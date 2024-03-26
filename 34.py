import cv2 as cv
import numpy as np
img=cv.imread('data\sudoku.png')
gray=cv.imread('data\sudoku.png',0)
edges=cv.Canny(gray,50,150,apertureSize=3)
lines=cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2=line[0]
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    
cv.imshow(' image',img)
cv.waitKey(0)
cv.destroyAllWindows()
