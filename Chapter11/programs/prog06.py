import numpy as np
import cv2
cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)
bg = cv2.imread('/home/pi/book/dataset/bg.jpg', 1)
print(bg.shape)
while ( True ):
    ret, frame = cap.read()
    print(frame.shape)
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    image_mask=cv2.inRange(hsv,np.array([40, 50, 50]),
                           np.array([80, 255, 255]))
    bg_mask=cv2.bitwise_and(bg, bg, mask=image_mask)
    fg_mask=cv2.bitwise_and(frame, frame,
                            mask=cv2.bitwise_not(image_mask))
#    cv2.imshow('Output', fg_mask)
    cv2.imshow('Output', cv2.add(bg_mask, fg_mask))
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()
