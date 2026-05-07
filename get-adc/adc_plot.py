import matplotlib.pyplot as plt


def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))

    plt.plot(time, voltage)

    plt.title("График зависимости напряжения от времени")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")

    plt.xlim(0, max(time))
    plt.ylim(0, max_voltage)

    plt.grid(True)
    plt.show()


def plot_measurement_duration_histogram(measurement_durations):
    plt.figure(figsize=(10, 6))

    plt.hist(measurement_durations, bins=20)

    plt.title("Распределение количества измерений по их продолжительности")
    plt.xlabel("Продолжительность измерения, с")
    plt.ylabel("Количество измерений")

    plt.grid(True)
    plt.show()