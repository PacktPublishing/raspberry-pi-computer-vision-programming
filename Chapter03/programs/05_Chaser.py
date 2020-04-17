#!/usr/bin/python3

from gpiozero import LED
from time import sleep

led1 = LED(2)
led2 = LED(3)
led3 = LED(4)
led4 = LED(17)
led5 = LED(27)
led6 = LED(22)
led7 = LED(10)
led8 = LED(9)
led9 = LED(11)

sleeptime = 0.2

while True:
	led1.on()
	sleep(sleeptime)
	led1.off()
	led2.on()
	sleep(sleeptime)
	led2.off()
	led3.on()
	sleep(sleeptime)
	led3.off()
	led4.on()
	sleep(sleeptime)
	led4.off()
	led5.on()
	sleep(sleeptime)
	led5.off()
	led6.on()
	sleep(sleeptime)
	led6.off()
	led7.on()
	sleep(sleeptime)
	led7.off()
	led8.on()
	sleep(sleeptime)
	led8.off()
	led9.on()
	sleep(sleeptime)
	led9.off()
