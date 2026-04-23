import RPi.GPIO as GPIO


class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose=False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")
            return

        if not (0 <= number <= 255):
            print("Число выходит за допустимый диапазон ЦАП (0-255)")
            print("Устанавливаем 0")
            number = 0

        bits = [int(bit) for bit in f"{number:08b}"]
        GPIO.output(self.gpio_bits, bits)

        if self.verbose:
            print(f"Число на вход ЦАП: {number}, биты: {bits}")

    def set_voltage(self, voltage):
        if not isinstance(voltage, (int, float)):
            print("Напряжение должно быть числом")
            return

        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            voltage = 0.0

        number = int(voltage / self.dynamic_range * 255)
        self.set_number(number)

        if self.verbose:
            print(f"Напряжение на выходе ЦАП: {voltage:.3f} В")