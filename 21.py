import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('data\sudoku.png',0)

lap=cv.Laplacian(img,cv.CV_64F,ksize=1)
lap=np.uint8(np.absolute(lap))
sobelx=cv.Sobel(img,cv.CV_64F,1,0)
sobely=cv.Sobel(img,cv.CV_64F,0,1)
sobelx=np.uint8(np.absolute(sobelx))
sobely=np.uint8(np.absolute(sobely))
sobelc=cv.bitwise_or(sobelx,sobely)

titles=['image','Laplacian','Sobel X','Sobel Y','Sobel Combo']
images=[img,lap,sobelx,sobely,sobelc]

for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()