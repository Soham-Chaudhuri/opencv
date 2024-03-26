import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

img=cv.imread('data\lane.jpg')
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
img=cv.GaussianBlur(img,(5,5),3)

print(img.shape)
height=img.shape[0]
width=img.shape[1]

region_of_interest_vertices=[
    (width/2,height),
    (width/2,height/2.25),
    (width,height/2.25),
    (width,height)
]

def region_of_interest(img,vertices):
    mask=np.zeros_like(img)
    # channel_count=img.shape[2]
    match_mask_color=255
    cv.fillPoly(mask,vertices,match_mask_color)
    masked_image=cv.bitwise_and(img,mask)
    return masked_image

gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
canny_image=cv.Canny(gray_img,150,150)

cropped_image=region_of_interest(canny_image,np.array([region_of_interest_vertices],np.int32))
plt.imshow(img)
plt.show()