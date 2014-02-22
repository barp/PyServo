#!/usr/bin/python

from pwm_drivers.Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
freq = 50

def setServoPulse(channel, pulse):
  pulseLength = 1000000.0                   # 1,000,000 us per second
  pulseLength /= freq                       # 60 Hz
  print("{:f} us per period".format(pulseLength))
  pulseLength /= 4096                     # 12 bits of resolution
  print("{:f} us per bit".format(pulseLength))
  pulse *= 1000
  pulse /= pulseLength
  print(pulse)
  pwm.setPWM(channel, 0, int(pulse))

pwm.setPWMFreq(freq)                        # Set frequency to 60 Hz
channel = 0

while True:
	setServoPulse(channel, 1.5)
	time.sleep(1)
	setServoPulse(channel, 0.6)
	time.sleep(1)
	setServoPulse(channel, 2.4)
	time.sleep(1)
