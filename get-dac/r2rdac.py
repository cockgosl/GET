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
        if not (0 <= number <= 255):
            print("Число выходит за допустимый диапазон ЦАП (0-255)")
            print("Устанавливаем 0 В")
            number = 0

        bits = [int(bit) for bit in f"{number:08b}"]
        GPIO.output(self.gpio_bits, bits)

        if self.verbose:
            print(f"Число на вход ЦАП: {number}, биты: {bits}")

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение за диапазоном ЦАП (0.0 - {self.dynamic_range:.2f} В)")
            print("Выставляем 0 В")
            number = 0
        else:
            number = int(voltage / self.dynamic_range * 255)

        self.set_number(number)


if __name__ == "__main__":
    dac = None

    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        if dac is not None:
            dac.deinit()