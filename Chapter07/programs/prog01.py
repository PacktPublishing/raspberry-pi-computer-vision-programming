import RPi.GPIO as GPIO
import cv2
import numpy as np
import random

p = 0.00

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
output = np.zeros(frame.shape, np.uint8)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

button1 = 7
button2 = 11

GPIO.setup(button1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, GPIO.PUD_UP)

while True:
    
    ret, frame = cap.read()
    
    button1_state = GPIO.input(button1)

    if button1_state == GPIO.LOW and p <= 0.1:
        p = p + 0.01
        
    if p > 0.1:
        p = 0.1

    button2_state = GPIO.input(button2)

    if button2_state == GPIO.LOW and p > 0:
        p = p - 0.01
    
    if p < 0:
        p = 0

    for i in range (frame.shape[0]):
        for j in range(frame.shape[1]):
            r = random.random()
            if r < p/2:
                output[i][j] = 0, 0, 0
            elif r < p:
                output[i][j] = 255, 255, 255
            else:
                output[i][j] = frame[i][j]

    print(p)
    cv2.imshow('Salt and pepper Noise App', output)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
