import RPi.GPIO as GPIO

dec_bits = [16, 20, 21, 25, 26, 17, 27, 22]
dynamic_range = 3.17


GPIO.setmode(GPIO.BCM)
GPIO.setup(dec_bits, GPIO.OUT, initial=GPIO.LOW)

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"напряжение выходит за динамический диапазон ЦАП(0.0-{dynamic_range:.2f} в)")
        print("Устанавливаем 0.0 В")
        return 0

    return int(voltage/dynamic_range * 255)

def number_to_dac(number):
    bits = [int(bit) for bit in f"{number:08b}"]
    GPIO.output(dec_bits, bits)
    print(f"Число на вход ЦАП: {number}, биты:{bits}")

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)
        except ValueError:
            print("вы ввели не число. Попробуйте ещё раз\n")

finally:
    GPIO.output(dec_bits, 0)
    GPIO.cleanup()