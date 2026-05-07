import time
import matplotlib.pyplot as plt

from mcp3021 import MCP3021


DYNAMIC_RANGE = 5.0
DURATION = 3.0


adc = MCP3021(dynamic_range=DYNAMIC_RANGE)

voltages = []
times = []
measurement_periods = []

try:
    start_time = time.time()

    while time.time() - start_time < DURATION:
        measurement_start_time = time.time()

        voltage = adc.get_voltage()

        measurement_end_time = time.time()

        current_time = measurement_end_time - start_time
        measurement_period = measurement_end_time - measurement_start_time

        times.append(current_time)
        voltages.append(voltage)
        measurement_periods.append(measurement_period)

        print(
            f"t = {current_time:.3f} с, "
            f"U = {voltage:.3f} В, "
            f"T = {measurement_period:.6f} с"
        )

    plt.figure()
    plt.plot(times, voltages)
    plt.title("График зависимости напряжения на входе АЦП от времени")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.grid(True)

    plt.figure()
    plt.hist(measurement_periods, bins=20)
    plt.title(
        "Распределение периодов дискретизации измерений\n"
        "по времени на одно измерение"
    )
    plt.xlabel("Период измерения, с")
    plt.ylabel("Количество измерений")
    plt.grid(True)

    plt.show()

finally:
    adc.deinit()