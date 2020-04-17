# sudo apt-get install python3-rpi.gpio
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)   # Ignore Warnings
GPIO.setmode(GPIO.BOARD)  # Use Physical Pin Numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
counter = 0

while True:
    if counter % 2 == 0:
        led1 = 8
        led2 = 10
    else:
        led1 = 10
        led2 = 8

    GPIO.output(led1, GPIO.HIGH)
    GPIO.output(led2, GPIO.LOW)
    sleep(1)
    counter = counter + 1
