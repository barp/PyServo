
from PyServo.pwm_drivers.Adafruit_PWM_Servo_Driver import PWM
from PyServo.utils.Singleton import Singleton

class ServoPWM(object, metaclass=Singleton):
    def __init__(self, address, debug=False):
        self._pwm = PWM(address, debug=debug)
        self._pwm.setPWMFreq(50)

    def getPWM(self):
        return self._pwm
