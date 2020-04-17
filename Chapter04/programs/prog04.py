import numpy as np
import cv2
def empty(z):
    pass
image = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('Palette')
cv2.createTrackbar('B', 'Palette', 0, 255, empty)
cv2.createTrackbar('G', 'Palette', 0, 255, empty)
cv2.createTrackbar('R', 'Palette', 0, 255, empty)
while(True):
    cv2.imshow('Palette', image)
    if cv2.waitKey(1) == 27 :
        break
    blue = cv2.getTrackbarPos('B', 'Palette')
    green = cv2.getTrackbarPos('G', 'Palette')
    red = cv2.getTrackbarPos('R', 'Palette')
    image[:] = [blue, green, red]
cv2.destroyWindow('Palette')
