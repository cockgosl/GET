from numpy import sin, pi, floor
from time import sleep


def get_sin_wave_amplitude(freq: float, time: float):
    return (sin(2.0 * pi * freq * time) + 1.0) / 2.0

def wait_for_sampling_period(sampling_frequency: float):
    sleep(1.0 / sampling_frequency)

def get_triangle_amplitude(freq: float, time: float):
    return abs(2.0 * (time * freq - floor(time * freq)) - 1)