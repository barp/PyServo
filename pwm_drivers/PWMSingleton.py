import pwm_drivers.Adafruit_PWM_Servo_Driver as PWM
import utils.singleton as singleton

@singleton.singleton
class PWMSingleton(object):
    def __init__(self, debug=False):
        self._pwm = PWM.PWM(0x40, debug=debug)

    def getPWM(self):
        return self._pwm
