import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('data\messi5.jpg',0)

canny=cv.Canny(img,100,200)



titles=['image','Canny']
images=[img,canny]

for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()


#canny edge detection steps
# noise reduction
# gradient calculation
# non-maximum supression
# double threshold
# edge tracking by hysteresis