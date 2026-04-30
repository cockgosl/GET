# ==================== r2r-sar.py ====================
from r2r_adc import R2R_ADC
import time
from adc_plot import plot_voltage_vs_time


DYNAMIC_RANGE = 3.3

adc = R2R_ADC(dynamic_range=DYNAMIC_RANGE, compare_time=0.0001)

voltage_values = []
time_values = []
duration = 3.0

try:
    start_time = time.time()

    while (time.time() - start_time) < duration:
        voltage = adc.get_sar_voltage()
        voltage_values.append(voltage)
        time_values.append(time.time() - start_time)

    plot_voltage_vs_time(time_values, voltage_values, DYNAMIC_RANGE)

finally:
    del adc