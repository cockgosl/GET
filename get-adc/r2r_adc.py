import RPi.GPIO as GPIO
import time


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def __del__(self):
        try:
            GPIO.output(self.bits_gpio, 0)
        except:
            pass
        finally:
            GPIO.cleanup()

    def number_to_dac(self, number):
        bits = [(number >> i) & 1 for i in range(7, -1, -1)]
        for pin, bit in zip(self.bits_gpio, bits):
            GPIO.output(pin, bit)
        if self.verbose:
            print(f"[DAC] {number} -> {bits}")

    def sequential_counting_adc(self):
        for number in range(256):
            self.number_to_dac(number)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == 1:
                return number
        return 255

    def get_sc_voltage(self):
        code = self.sequential_counting_adc()
        return (code / 255.0) * self.dynamic_range


if __name__ == "__main__":
    try:
        adc = R2R_ADC(dynamic_range=3.3)
        while True:
            voltage = adc.get_sc_voltage()
            print(f"Напряжение: {voltage:.3f} В")
            time.sleep(0.5)
    finally:
        del adc