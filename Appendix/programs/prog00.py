import cv2

cv2.setUseOptimized(True)
print(cv2.useOptimized())
img = cv2.imread('/home/pi/book/dataset/4.1.01.tiff', 0)
e1 = cv2.getTickCount()
img1 = cv2.medianBlur(img, 23)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print(t)
