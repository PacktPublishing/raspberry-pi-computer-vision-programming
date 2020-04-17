import cv2
import matplotlib.pyplot as plt
img = cv2.imread('/home/pi/book/dataset/4.1.05.tiff', 0)
laplacian = cv2.Laplacian(img, ddepth=cv2.CV_32F, ksize=17,
                          scale=1, delta=0,
                          borderType=cv2.BORDER_DEFAULT)
sobel = cv2.Sobel(img, ddepth=cv2.CV_32F, dx=1, dy=0,
                  ksize=11, scale=1, delta=0,
                  borderType=cv2.BORDER_DEFAULT)
scharr = cv2.Scharr(img, ddepth=cv2.CV_32F, dx=1, dy=0,
                    scale=1, delta=0,
                    borderType=cv2.BORDER_DEFAULT)
images=[img, laplacian, sobel, scharr]
titles=['Original', 'Laplacian', 'Sobel', 'Scharr']
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], cmap = 'gray')
    plt.title(titles[i])
    plt.axis('off')
plt.show()
