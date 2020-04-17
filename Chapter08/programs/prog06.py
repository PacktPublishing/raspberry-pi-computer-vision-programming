import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 250, apertureSize=5,
                      L2gradient=True)
    lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
    if lines is not None:
        for rho,theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            pts1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pts2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(img, pts1, pts2, (0, 0, 255), 2)
    cv2.imshow('Detected Lines', img)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
cap.release()
