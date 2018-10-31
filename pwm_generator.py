import RPi.GPIO as GPIO
import time


class PwmGenerator(object):
    """
    synopsis   : Generate the PWM signal based on the given information
                 One instance controls one PIN
    require    : python 3.5 or later

    pin        : Output target GPIO pin (Raspberry pi)
    power      : Power ratio (0.0 ~ 1.0)
    frequency  : Frequency of PWM signal (Hz / default: 200Hz)
    """

    def __init__(self, pin: int = -1, power: float = 0, frequency: int = 200):
        self.pin = pin
        self.power = power
        assert self.frequency >= 2
        self.frequency = frequency
        self.status = False

    @property
    def get_status(self) -> bool:
        return self.status

    @property
    def get_power(self) -> float:
        return self.power

    @set_power.setter
    def set_power(self, power: float):
        assert isinstance(power, float)
        self.power = power

    def start(self):
        # GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

        if not self.status:
            self.status = True
            GPIO.output(self.pin, True)
            time.sleep(1)

        for sec_counter in range(self.frequency):
            on_time = (1 / self.frequency) * (self.power / 100)
            off_time = (1 / self.frequency) - time_on

            while True:
                GPIO.output(self.pin, True)
                time.sleep(on_time)

                if self.power != 1.0:
                    GPIO.output(self.pin, False)
                    time.sleep(off_time)

    def stop(self):
        self.status = False
        GPIO.output(self.pin, False)
        GPIO.cleanup(self.pin)
