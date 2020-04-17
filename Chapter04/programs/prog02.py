import cv2
img = cv2.imread('/home/pi/book/dataset/4.2.03.tiff', 0)

import matplotlib.pyplot as plt
plt.imshow(img, cmap='gray')
plt.title('Mandrill')
plt.axis('off')
plt.show()