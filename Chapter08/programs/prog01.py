import RPi.GPIO as GPIO
import cv2

x = 0
y = 1

cap = cv2.VideoCapture(0)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

button1 = 7
button2 = 11

GPIO.setup(button1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, GPIO.PUD_UP)

while True:
    print(x, y)
    ret, frame = cap.read()
    
    button1_state = GPIO.input(button1)

    if button1_state == GPIO.LOW:
        x = 0
        y = 1

    button2_state = GPIO.input(button2)

    if button2_state == GPIO.LOW:
        x = 1
        y = 0

    output = cv2.Scharr(frame, ddepth=cv2.CV_32F,
                        dx=x, dy=y,
                        scale=1, delta=0,
                        borderType=cv2.BORDER_DEFAULT)

    
    cv2.imshow('Salt and pepper Noise App', output)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

