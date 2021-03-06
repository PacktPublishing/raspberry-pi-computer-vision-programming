# sudo apt-get install python3-rpi.gpio
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)   # Ignore Warnings
GPIO.setmode(GPIO.BOARD)  # Use Physical Pin Numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

while True:
    GPIO.output(8, GPIO.HIGH)
    sleep(1)
    GPIO.output(8, GPIO.LOW)
    sleep(1)
