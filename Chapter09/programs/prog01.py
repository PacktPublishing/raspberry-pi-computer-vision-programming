import cv2
import pymeanshift as pms
from matplotlib import pyplot as plt
img = cv2.imread('/home/pi/book/dataset/house.tiff', 1)
input = cv2.cvtColor(img, cv2.COLOR_BGR2RGB )
(segmented_image, labels_image, number_regions) = pms.segment(
    input, spatial_radius=2, range_radius=2, min_density=300)

plt.subplot(131)
plt.imshow(input)
plt.title('Input')
plt.axis('off')

plt.subplot(132)
plt.imshow(segmented_image)
plt.title('Segmented Output')
plt.axis('off')

plt.subplot(133)
plt.imshow(labels_image)
plt.title('Labeled Output')
plt.axis('off')

plt.show()
