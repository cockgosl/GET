import time
import matplotlib.pyplot as plt

from mcp3021_driver import MCP3021


DYNAMIC_RANGE = 5.0
DURATION = 10.0


adc = MCP3021(dynamic_range=DYNAMIC_RANGE)

voltage_values = []
time_values = []
measurement_durations = []

try:
    start_time = time.time()

    while time.time() - start_time < DURATION:
        measurement_start_time = time.time()

        voltage = adc.get_voltage()

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

    plt.figure(figsize=(10, 6))
    plt.plot(time_values, voltage_values)
    plt.title("График зависимости напряжения на входе MCP3021 от времени")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.xlim(0, max(time_values))
    plt.ylim(0, DYNAMIC_RANGE)
    plt.grid(True)

    plt.figure(figsize=(10, 6))
    plt.hist(measurement_durations, bins=20)
    plt.title("Распределение количества измерений по их продолжительности")
    plt.xlabel("Продолжительность измерения, с")
    plt.ylabel("Количество измерений")
    plt.grid(True)

    plt.show()

finally:
    try:
        adc.deinit()
    except OSError:
        pass