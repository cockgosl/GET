import math
import time
import r2r_dac as r2r


amplitude = 3.0
signal_frequency = 10
sampling_frequency = 1000


if __name__ == "__main__":
    dac = None

    try:
        dac = r2r.R2R_DAC([26, 19, 13, 6, 5, 11, 9, 10], 3.3, verbose=False)

        samples_per_period = int(sampling_frequency / signal_frequency)

        while True:
            for n in range(samples_per_period):
                normalized_amplitude = (math.sin(2 * math.pi * n / samples_per_period) + 1) / 2
                voltage = normalized_amplitude * amplitude

                dac.set_voltage(voltage)
                time.sleep(1 / sampling_frequency)

    except KeyboardInterrupt:
        print("\nГенерация сигнала остановлена пользователем")

    finally:
        if dac is not None:
            dac.deinit()