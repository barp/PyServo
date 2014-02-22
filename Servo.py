import pwm_drivers.ServoPWM as PWM

class Servo(object):
    """controls a servo"""
    FREQ = 50.0
    def __init__(self, channel, quality=4096, start=0.5, end=2.5, debug=False):
       self._channel = channel
       self._debug = debug
       self._quality = quality
       self._pwm = PWM.ServoPWM(0x40, debug=debug).getPWM()

    def _setServoPulse(self, miliseconds):
        frame_size = 1000.0 / Servo.FREQ
        tick_size = frame_size / self._quality
        pulse = int(miliseconds / tick_size)
        self._pwm.setPWM(self._channel, 0, pulse)

    def setAngle(self, angle):
        angle = (angle / 180.0) * 2 + 0.5
        self._setServoPulse(angle)
