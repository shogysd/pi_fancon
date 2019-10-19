from subprocess import getoutput


class PowerAdjustment(object):
    """
    Calculate fan output from CPU temperature
    ----------
    power level
      T <= 40'C        : power 0.0
      40'C < T <= 50'C : power 0.5
      50'C < T <= 60'C : power 0.7
      60'C < T <= 70'C : power 1.0
      70'C <           : power -1.0 (emg stop)
    """

    def __init__(self):
        self.power = 0.0

    def update_power(self):
        cpu_temp = float(getoutput("vcgencmd measure_temp").split("=")[1].split("'")[0])
        if cpu_temp <= 40:
            self.power = 0.0
        elif cpu_temp <= 50:
            self.power = 0.5
        elif cpu_temp <= 60:
            self.power = 0.7
        elif cpu_temp <= 70:
            self.power = 1.0
        else:
            self.power = -1.0

    def get_power(self) -> float:
        self.update_power()
        return self.power
