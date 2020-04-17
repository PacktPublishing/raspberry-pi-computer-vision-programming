import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False

print(ret)
print(type(frame))
cv2.imshow('Frame from Webcam', frame)
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
