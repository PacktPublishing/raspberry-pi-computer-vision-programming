import numpy as np
import cv2
import random
import matplotlib.pyplot as plt
img = cv2.imread('/home/pi/book/dataset/4.1.03.tiff', 0)
output = np.zeros(img.shape, np.uint8)
p = 0.05
for i in range (img.shape[0]):
    for j in range(img.shape[1]):
        r = random.random()
        if r < p/2:
            output[i][j] = 0
        elif r < p:
            output[i][j] = 255
        else:
            output[i][j] = img[i][j]
plt.imshow(output, cmap='gray')
plt.title('Salt and Pepper Sprinkled')
plt.axis('off')
plt.show()
