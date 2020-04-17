import time
import cv2

cap = cv2.VideoCapture(0)

fps = cap.get(cv2.CAP_PROP_FPS)
print("FPS with CAP_PROP_FPS : {0}".format(fps))

num_frames = 120
print("Capturing {0} frames".format(num_frames))

start = time.time()
for i in range(0, num_frames):
    ret, frame = cap.read()
end = time.time()

seconds = end - start
print("Time taken : {0} seconds".format(seconds))

fps = num_frames / seconds
print("Actual FPS calculated : {0}".format(fps))

cap.release()
