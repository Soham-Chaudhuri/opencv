import cv2
import numpy as np
# img=cv2.imread('data\lena.jpg',1)
img=np.zeros([512,512,3],np.uint8)
img=cv2.line(img,(0,0),(255,255),(0,255,0),3) #(img,pt1,pt2,bgr(),thickness)
img=cv2.rectangle(img,(0,0),(200,200),(0,0,255),4)
img=cv2.circle(img,(255,255),25,(0,255,0),-1)
img=cv2.putText(img,'OpenCV',(10,500),cv2.FONT_HERSHEY_SIMPLEX,4,(0,180,255),10,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()