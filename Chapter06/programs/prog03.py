import cv2
import numpy as np
c = cv2.cvtColor(np.array([[[255, 0, 0]]],
                          dtype=np.uint8),
                 cv2.COLOR_BGR2HSV)
print(c)
