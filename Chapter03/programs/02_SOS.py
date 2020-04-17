# sudo apt-get install python3-rpi.gpio
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)   # Ignore Warnings
GPIO.setmode(GPIO.BOARD)  # Use Physical Pin Numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

def flash(led, duration):
    GPIO.output(led, GPIO.HIGH)
    sleep(duration)
    GPIO.output(led, GPIO.LOW)
    sleep(duration)

while True:
    flash(8, 0.2)
    flash(8, 0.2)
    flash(8, 0.2)
    sleep(0.3)

    flash(8, 0.5)
    flash(8, 0.5)
    flash(8, 0.5)
    
    flash(8, 0.2)
    flash(8, 0.2)
    flash(8, 0.2)
    sleep(1)
