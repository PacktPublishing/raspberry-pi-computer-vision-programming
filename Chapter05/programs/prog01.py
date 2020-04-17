import cv2
img1 = cv2.imread('/home/pi/book/dataset/4.2.03.tiff', 1)
img2 = cv2.imread('/home/pi/book/dataset/4.2.05.tiff', 1)
cv2.imshow('NumPy Addition', img1 + img2 )
cv2.imshow('OpenCV Addition', cv2.add(img1, img2))
cv2.waitKey(0)
cv2.destroyAllWindows()
