import time
import matplotlib.pyplot as plt

from mcp3021_driver import MCP3021


DYNAMIC_RANGE = 5.0
DURATION = 3.0


adc = MCP3021(dynamic_range=DYNAMIC_RANGE)

voltage_values = []
time_values = []
measurement_durations = []

try:
    start_time = time.time()

    while time.time() - start_time < DURATION:
        measurement_start_time = time.time()

        voltage = adc.get_voltage()

        measurement