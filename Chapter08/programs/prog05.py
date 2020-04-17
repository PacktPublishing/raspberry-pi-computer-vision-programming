import cv2
cap = cv2.VideoCapture(0)
while (True):
    ret , frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(grey, (5, 5))
    circles = cv2.HoughCircles(blur,
                               method=cv2.HOUGH_GRADIENT,
                               dp=1, minDist=200,
                               param1=50, param2=13,
                               minRadius=30, maxRadius=175)
    if circles is not None:
        for i in circles [0,:]:
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)
    cv2.imshow('Detected', frame)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
cap.release()
