import cv2
cap=cv2.VideoCapture(1);
# fourcc=cv2.VideoWriter_fourcc(*'XVID')
# out=cv2.VideoWriter('output.avi',fourcc,35,(640,480))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3,320)#width has 3 property number
cap.set(4,240)#height has 4 property number
print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        
        # out.write(frame)
        if cv2.waitKey(1)==ord('q'):
            break
    else:
        break

cap.release()
# out.release()
cv2.destroyAllWindows()