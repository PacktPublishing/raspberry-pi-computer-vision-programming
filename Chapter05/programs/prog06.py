import time
import RPi.GPIO as GPIO
import cv2

alpha = 0

img1 = cv2.imread('/home/pi/book/dataset/4.2.03.tiff', 1)
img2 = cv2.imread('/home/pi/book/dataset/4.2.05.tiff', 1)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

button1 = 7
button2 = 11

GPIO.setup(button1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, GPIO.PUD_UP)

while True:
    button1_state = GPIO.input(button1)

    if button1_state == GPIO.LOW and alpha < 1:
        alpha = alpha + 0.2

    button2_state = GPIO.input(button2)

    if button2_state == GPIO.LOW:
        if (alpha > 0):
            alpha = alpha - 0.2
            
    if (alpha < 0):
        alpha = 0

    beta = 1 - alpha

    output = cv2.addWeighted(img1, alpha, img2, beta, 0)
    cv2.imshow('Transition App', output)
    if cv2.waitKey(1) == 27:
        break

    time.sleep(0.5)
    print(alpha)
cv2.destroyAllWindows()
