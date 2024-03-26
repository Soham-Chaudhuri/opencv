#edge detection
#mapping edge points
#interpretation to inf lines
#inf to finite lines
import cv2 as cv
import numpy as np
img=cv.imread('data\sudoku.png')
gray=cv.imread('data\sudoku.png',0)
edges=cv.Canny(gray,50,150,apertureSize=3)
lines=cv.HoughLines(edges,1,np.pi/180,200)

for line in lines:
    rho,theta=line[0]
    a=np.cos(theta)
    b=np.sin(theta)
    x0=a*rho
    y0=b*rho
    x1=int(x0+1000*(-b))
    y1=int(y0+1000*(a))
    x2=int(x0-1000*(-b))
    y2=int(y0-1000*(a))
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    
cv.imshow(' image',img)
cv.waitKey(0)
cv.destroyAllWindows()


# Certainly. This segment of the code calculates two points, `(x1, y1)` and `(x2, y2)`, which are used to draw the detected line on the image. The line is represented in the Hough transform using polar coordinates `(rho, theta)`, where:

# - `rho` is the perpendicular distance from the origin (top-left of the image) to the line.
# - `theta` is the angle between the x-axis (horizontal axis) and the line drawn to the origin (which is perpendicular to the detected line).

# Given `rho` and `theta`, you can derive the direction in which the line is oriented using trigonometry:

# - `a = cos(theta)`
# - `b = sin(theta)`

# The point `(x0, y0)` is a point on the detected line:

# - `x0 = rho * cos(theta)`
# - `y0 = rho * sin(theta)`

# This `(x0, y0)` point, however, isn't enough to draw the line; you need a start and an end point. This is where `(x1, y1)` and `(x2, y2)` come in.

# To find these points, the idea is to move a certain distance along the line's normal and anti-normal direction (perpendicular to the line).

# Here's the breakdown:

# 1. **Calculating (x1, y1)**:
#     - `x1 = x0 + 1000 * (-b)`
#     - `y1 = y0 + 1000 * (a)`

#    Here, you're moving 1000 units in the normal direction of the line. If you visualize this, it's like stepping 1000 units in a direction perpendicular to the detected line from the point `(x0, y0)`.

# 2. **Calculating (x2, y2)**:
#     - `x2 = x0 - 1000 * (-b)`
#     - `y2 = y0 - 1000 * (a)`

#    Here, you're moving 1000 units in the opposite direction (anti-normal). 

# By choosing a large number like 1000, you ensure that the lines are drawn well outside the image area, ensuring they extend across the entire image. In practice, these lines will be clipped to the image boundaries.

# In summary, `(x1, y1)` and `(x2, y2)` are two distant points on the detected line, and when connected, they'll give the appearance of an infinite line across the image.