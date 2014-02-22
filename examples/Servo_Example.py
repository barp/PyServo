#!/usr/bin/python3

from PyServo.Servo import Servo
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
servo = Servo(0, debug=True)

while True:
	servo.setAngle(90)
	time.sleep(1)
	servo.setAngle(0)
	time.sleep(1)
	servo.setAngle(180)
	time.sleep(1)
