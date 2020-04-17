import cv2
img = cv2.imread('/home/pi/book/dataset/4.2.03.tiff', 1)
cv2.imshow('Mandrill', img)
cv2.waitKey(0)
cv2.destroyWindow('Mandrill')
