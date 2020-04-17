import cv2
img = cv2.imread('/home/pi/book/dataset/4.2.03.tiff', 1)
cv2.imshow('Mandrill', img)
keyPress = cv2.waitKey(0)
if keyPress == ord('q'):
    cv2.destroyWindow('Mandrill')
elif keyPress == ord('s'):
    cv2.imwrite('test.jpg', img)
    cv2.destroyWindow('Mandrill')
