import signal_generator as sg
from mcp4725_driver import MCP4725
from time import time


amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000


if __name__ == "__main__":
    try:
        dac = MCP4725(5)
        while True:
            dac.set_voltage(amplitude * sg.get_triangle_amplitude(signal_frequency, time()))
            sg.wait_for_sampling_period(sampling_frequency)
    finally:
        dac.deinit()