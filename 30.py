import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
# img=np.zeros((200,200),np.uint8)
img=cv.imread('data\lena.jpg')
cv.imshow('img',img)
hist=cv.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
# plt.hist(img.ravel(),256,[0,256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()