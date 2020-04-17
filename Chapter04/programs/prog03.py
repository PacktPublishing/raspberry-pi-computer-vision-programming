import cv2
import numpy as np
image = np.zeros((200, 200, 3), np.uint8)
cv2.line(image, (0, 199), (199, 0), (0, 0, 255), 2)
cv2.rectangle(image, (20, 20), (60, 60), (255, 0, 0), 1)
cv2.circle(image, (80, 80), 10, (0, 255, 0), -1)
cv2.ellipse(image, (99, 99), (40, 20), 0, 0, 360, (128, 128, 128), -1)
points = np.array([[100, 5], [125, 30], [175, 20], [185, 10]], np.int32)
points = points.reshape((-1, 1, 2))
cv2.polylines(image, [points], True, (255, 255, 0))
cv2.putText(image, 'Test', (80, 180), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255))
cv2.imshow('Shapes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
