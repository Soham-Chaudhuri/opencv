import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('data\sudoku.png')

cv.imshow('sudoku',img)
plt.xticks([])
plt.yticks([])
plt.imshow(img)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()



#cv reads the image in BGR format and matplotlib shows the image in BGR
