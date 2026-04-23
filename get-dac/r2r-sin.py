import signal_generator as sg
from r2r_dac import R2R_DAC
from time import time


amplitude = 3.1
signal_frequency = 10
sampling_frequency = 1000


if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3)
        while True:
            dac.set_voltage(amplitude * sg.get_sin_wave_amplitude(signal_frequency, time()))
            sg.wait_for_sampling_period(sampling_frequency)
    finally:
        dac.deinit()