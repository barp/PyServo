import pwm_drivers.Adafruit_PWM_Servo_Driver as PWM

class Servo(object):
    """controls a servo"""
    def __init__(self, channel, start=0.5, end=2.5, debug=False):
       self._channel = channel
       self._debug = debug
       self._pwm = PWM.PWM(0x40, debug=debug)
