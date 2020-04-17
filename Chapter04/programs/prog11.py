import cv2

windowName = "OpenCV Video Player"
cv2.namedWindow(windowName)
filename = 'output.avi'
cap = cv2.VideoCapture(filename)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.imshow(windowName, frame)
        if cv2.waitKey(33) == 27:
            break
    else:
        break

cv2.destroyAllWindows()
cap.release()

