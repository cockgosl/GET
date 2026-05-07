import time

from r2r_adc import R2R_ADC
from adc_plot import plot_voltage_vs_time
from adc_plot import plot_measurement_duration_histogram


DYNAMIC_RANGE = 3.3
DURATION = 3.0


adc = R2R_ADC(
    dynamic_range=DYNAMIC_RANGE,
    compare_time=0.0001
)

voltage_values = []
time_values = []
measurement_durations = []

try:
    start_time = time.time()

    while time.time() - start_time < DURATION:
        measurement_start_time = time.time()

        voltage = adc.get_sar_voltage()

        measurement_end_time = time.time()

        current_time = measurement_end_time - start_time
        measurement_duration = measurement_end_time - measurement_start_time

        voltage_values.append(voltage)
        time_values.append(current_time)
        measurement_durations.append(measurement_duration)

        print(
            f"t = {current_time:.3f} с, "
            f"U = {voltage:.3f} В, "
            f"T = {measurement_duration:.6f} с"
        )

    plot_voltage_vs_time(
        time_values,
        voltage_values,
        DYNAMIC_RANGE
    )

    plot_measurement_duration_histogram(
        measurement_durations
    )

finally:
    adc.deinit()