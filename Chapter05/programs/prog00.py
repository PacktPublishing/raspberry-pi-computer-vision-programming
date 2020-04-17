import cv2
img = cv2.imread('/home/pi/book/dataset/4.1.01.tiff', 1)
b1 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_WRAP)
b2 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[255, 0, 0])
cv2.imshow('Wrap', b1)
cv2.imshow('Constant', b2)
cv2.waitKey(0)
cv2.destroyAllWindows()
