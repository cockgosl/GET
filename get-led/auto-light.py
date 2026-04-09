import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

led = 26

GPIO.setup(led, GPIO.OUT)

divider = 6

GPIO.setup(divider, GPIO.IN)

while True:
    sensor_state = GPIO.input(divider)
    GPIO.output(led, not sensor_state)
    time.sleep(0.01)
