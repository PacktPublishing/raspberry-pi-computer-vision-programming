import cv2

def emptyFunction():
    pass

img = cv2.imread('/home/pi/book/dataset/4.2.07.tiff', 1)

windowName = "Saturation Demo"
cv2.namedWindow(windowName)
cv2.createTrackbar('Saturation Level',
                   windowName, 0, 
                   24, emptyFunction)
while(True):
    hsv = cv2.cvtColor( img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    saturation = cv2.getTrackbarPos('Saturation Level', windowName)
    s = s + saturation
    v = v + saturation
    img1 = cv2.cvtColor(cv2.merge((h, s, v)), cv2.COLOR_HSV2BGR)
    cv2.imshow(windowName, img1)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
