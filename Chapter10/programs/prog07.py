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

kernel = np.ones((3, 3), np.uint8)

erosion = cv2.erode(img, kernel, iterations = 1)
dilation = cv2.dilate(img, kernel, iterations = 1)
gradient = cv2.morphologyEx(img,
                            cv2.MORPH_GRADIENT,
                            kernel)
titles=['Original', 'Erosion',
        'Dilation', 'Gradient']
output=[img, erosion, dilation, gradient]
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(output[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.show()
