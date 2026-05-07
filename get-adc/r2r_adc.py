import RPi.GPIO as GPIO
import time


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.001, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def __del__(self):
        try:
            self.deinit()
        except Exception:
            pass

    def number_to_dac(self, number):
        bits = [(number >> i) & 1 for i in range(7, -1, -1)]
        GPIO.output(self.bits_gpio, bits)

        if self.verbose:
            print(f"[DAC] {number} -> {bits}")

    def sequential_counting_adc(self):
        for number in range(256):
            self.number_to_dac(number)
            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio) == 1:
                time.sleep(self.compare_time * 5)
                self.number_to_dac(0)
                time.sleep(self.compare_time * 2)
                return number

        self.number_to_dac(0)
        return 255

    def get_sc_voltage(self):
        code = self.sequential_counting_adc()
        voltage = (code / 255.0) * self.dynamic_range
        return voltage

    def successive_approximation_adc(self):
        result = 0

        for bit in range(7, -1, -1):
            test_number = result | (1 << bit)

            self.number_to_dac(test_number)
            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio) == 0:
                result = test_number

            if self.verbose:
                print(
                    f"[SAR] bit={bit}, "
                    f"test={test_number}, "
                    f"result={result}, "
                    f"comp={GPIO.input(self.comp_gpio)}"
                )

        self.number_to_dac(0)
        return result

    def get_sar_voltage(self):
        code = self.successive_approximation_adc()
        voltage = (code / 255.0) * self.dynamic_range
        return voltage


if __name__ == "__main__":
    adc = R2R_ADC(dynamic_range=3.3, compare_time=0.001)

    try:
        while True:
            voltage = adc.get_sar_voltage()
            print(f"Напряжение: {voltage:.3f} В")

    finally:
        adc.deinit()