import cv2
img = cv2.imread('/home/pi/book/dataset/4.2.07.tiff', 0)
negative = abs(255 - img)
cv2.imshow('Grayscale', img)
cv2.imshow('Negative', negative)
cv2.waitKey(0)
cv2.destroyAllWindows()
