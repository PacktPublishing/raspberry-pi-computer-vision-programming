import cv2

cv2.namedWindow('Canny')
img = cv2.imread('/home/pi/book/dataset/4.1.05.tiff', 0)

def empty(z):
    pass

cv2.createTrackbar('Threshold 1', 'Canny', 50, 100, empty)
cv2.createTrackbar('Threshold 2', 'Canny', 150, 300, empty)

while(True):

    l1 = cv2.getTrackbarPos('Threshold 1', 'Canny')
    l2 = cv2.getTrackbarPos('Threshold 2', 'Canny')

    output = cv2.Canny(img, l1, l2, L2gradient=False)
    
    cv2.imshow('Canny', output)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
