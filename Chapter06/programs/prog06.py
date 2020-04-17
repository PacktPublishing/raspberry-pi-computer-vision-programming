import numpy as np
import cv2
def emptyFunction():
    pass
cap = cv2.VideoCapture(0)
windowName = 'Object Tracker'
trackbarName = 'Color Chooser'
cv2.namedWindow(windowName)
cv2.createTrackbar(trackbarName,
                   windowName, 0, 1,
                   emptyFunction)
color = 0
while ( True ):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    color = cv2.getTrackbarPos(trackbarName, windowName)
    if color == 0:
        image_mask = cv2.inRange(hsv, np.array([40, 50, 50]),
                                 np.array([80, 255, 255]))
    else:
        image_mask = cv2.inRange(hsv, np.array([100, 50, 50]),
                                 np.array([140, 255, 255]))        
    output = cv2.bitwise_and(frame, frame, mask=image_mask)
    cv2.imshow(windowName, output)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
cap.release()
