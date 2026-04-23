import r2rdac as r2r
import signal_generator as sg
import time


amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000


if __name__ == "__main__":
    dac = None

    try:
        dac = r2r.R2R_DAC([26, 19, 13, 6, 5, 11, 9, 10], 3.3, verbose=False)

        start_time = time.time()

        while True:
            current_time = time.time() - start_time

            normalized_amplitude = sg.get_sin_wave_amplitude(signal_frequency, current_time)
            voltage = normalized_amplitude * amplitude

            dac.set_voltage(voltage)

            sg.wait_for_sampling_period(sampling_frequency)

    except KeyboardInterrupt:
        print("\nГенерация сигнала остановлена пользователем")

    finally:
        if dac is not None:
            dac.deinit()