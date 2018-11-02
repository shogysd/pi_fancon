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
    runtime    : Time to continue output (sec)
    """

    def __init__(self, pin: int = -1, power: float = 0.0, frequency: int = 200, runtime: int = 1):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        self.power = power
        assert frequency >= 2
        self.frequency = frequency
        assert isinstance(runtime, int)
        self.runtime = runtime
        self.status = False

    def get_status(self) -> bool:
        return self.status

    def get_power(self) -> float:
        return self.power

    def set_power(self, power: float):
        assert isinstance(power, float)
        self.power = power

    def start(self):

        if self.power == 0.0:
            self.status = False
            GPIO.output(self.pin, False)
            time.sleep(self.runtime)

        elif self.power == 1.0:
            self.status = True
            GPIO.output(self.pin, True)
            time.sleep(self.runtime)

        else:
            on_time = (1 / self.frequency) * self.power
            off_time = (1 / self.frequency) - on_time

            if not self.status:
                GPIO.output(self.pin, True)
                time.sleep(0.5)
            self.status = True

            for i in range(self.runtime):

                for sec_counter in range(self.frequency):
                    GPIO.output(self.pin, True)
                    time.sleep(on_time)
                    GPIO.output(self.pin, False)
                    time.sleep(off_time)

    def stop(self):
        self.status = False
        GPIO.output(self.pin, False)
        GPIO.cleanup(self.pin)
