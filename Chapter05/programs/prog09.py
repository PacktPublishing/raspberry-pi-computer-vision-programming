import cv2
import numpy as np
import matplotlib.pyplot as plt
a = [0, 255, 0]
img1 = np.array([a, a, a], dtype=np.uint8)
img2 = np.transpose(img1)
not_out = cv2.bitwise_not(img1 )
and_out = cv2.bitwise_and(img1, img2)
or_out = cv2.bitwise_or(img1, img2)
xor_out = cv2.bitwise_xor(img1, img2)
titles = ['Image 1', 'Image 2', 'Image 1 NOT', 'AND', 'OR', 'XOR']
images = [img1, img2, not_out, and_out, or_out, xor_out]
for i in range(6):
	plt.subplot(2, 3, i+1)
	plt.imshow(images[i], cmap='gray')
	plt.title(titles[i])
	plt.axis('off')
plt.show()
