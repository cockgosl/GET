import signal_generator as sg
from pwm_dac import PWM_DAC
from time import time


amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000


if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.2)
        while True:
            dac.set_voltage(amplitude * sg.get_triangle_amplitude(signal_frequency, time()))
            sg.wait_for_sampling_period(sampling_frequency)
    finally:
        dac.deinit()