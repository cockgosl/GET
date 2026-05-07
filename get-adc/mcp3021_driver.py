import smbus
import time


class MCP3021:
    def __init__(self, dynamic_range, address=0x4D, verbose=False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = address
        self.verbose = verbose

    def deinit(self):
        try:
            self.bus.close()
        except OSError:
            pass

    def get_number(self):
        try:
            upper_data_byte = self.bus.read_byte(self.address)
            lower_data_byte = self.bus.read_byte(self.address)

            number = ((upper_data_byte << 8) | lower_data_byte) >> 2
            number = number & 0x3FF

            if self.verbose:
                print(
                    f"Старший байт: {upper_data_byte:02x}, "
                    f"Младший байт: {lower_data_byte:02x}, "
                    f"Число: {number}"
                )

            return number

        except OSError as error:
            print(f"Ошибка I2C: {error}")
            return 0

    def get_voltage(self):
        number = self.get_number()
        voltage = (number / 1023.0) * self.dynamic_range
        return voltage


if __name__ == "__main__":
    adc = MCP3021(dynamic_range=5.0, verbose=True)

    try:
        while True:
            voltage = adc.get_voltage()
            print(f"Напряжение: {voltage:.3f} В")
            time.sleep(1)

    finally:
        adc.deinit()