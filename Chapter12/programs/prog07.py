import cv2
import numpy as np
import mahotas as mh

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    T_otsu = mh.otsu(frame)
    output = frame > T_otsu
    output = output.astype(np.uint8) * 255
    cv2.imshow('Sepia', output)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()
