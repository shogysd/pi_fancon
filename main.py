from power_adjustment import PowerAdjustment
from pwm_generator import PwmGenerator
import RPi.GPIO as GPIO

import time


def main():

    GPIO.setmode(GPIO.BCM)
    power = PowerAdjustment()

    signal = PwmGenerator(18, 0, 200, 5)

    signal.set_power(power.get_power())

    signal.start()
    signal.stop()


if __name__ == '__main__':
    main()
