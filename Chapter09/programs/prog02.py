import cv2
import pymeanshift as pms

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    (segmented_image, labels_image, number_regions) = pms.segment(
        frame, spatial_radius=2, range_radius=2, min_density=50)
    
    cv2.imshow('Segmented', segmented_image)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
cap.release()
