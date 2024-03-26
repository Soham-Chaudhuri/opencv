import cv2
cap=cv2.VideoCapture(1);
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,35,(640,480))
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        if cv2.waitKey(1)==ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()