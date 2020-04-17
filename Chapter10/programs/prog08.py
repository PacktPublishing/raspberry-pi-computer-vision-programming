import numpy as np
import cv2
from matplotlib import pyplot as plt

img = np.array([[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 255, 255, 255, 0, 0],
                [0, 0, 255, 255, 255, 0, 0],
                [0, 0, 255, 255, 255, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]], dtype=np.uint8)

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

open = cv2.morphologyEx(img,
                        cv2.MORPH_OPEN,
                        kernel)
close = cv2.morphologyEx(img,
                        cv2.MORPH_CLOSE,
                        kernel)
tophat = cv2.morphologyEx(img,
                        cv2.MORPH_TOPHAT,
                        kernel)
blackhat = cv2.morphologyEx(img,
                        cv2.MORPH_BLACKHAT,
                        kernel)
hitmiss = cv2.morphologyEx(img,
                        cv2.MORPH_HITMISS,
                        kernel)

titles=['Original', 'Open',
        'Close', 'Top hat',
        'Black hat', 'Hit Miss']
output=[img, open, close,
        tophat, blackhat,
        hitmiss]
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(output[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.show()
