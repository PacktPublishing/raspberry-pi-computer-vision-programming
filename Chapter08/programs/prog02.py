import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    output1 = cv2.Scharr(frame, ddepth=cv2.CV_32F,
                        dx=0, dy=1,
                        scale=1, delta=0,
                        borderType=cv2.BORDER_DEFAULT)
    
    output2 = cv2.Scharr(frame, ddepth=cv2.CV_32F,
                        dx=1, dy=0,
                        scale=1, delta=0,
                        borderType=cv2.BORDER_DEFAULT)
    cv2.imshow('Addition of Vertical and Horizontal',
               cv2.add(output1, output2))
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()

