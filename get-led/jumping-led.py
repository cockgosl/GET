import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

bit_c = 12

leds = [24, 22, 23, 27, 17, 25, 12, 16]

GPIO.setup(leds, GPIO.OUT)

GPIO.setup(leds, 0)

light_time = 0.2

while True:
        for led in leds:
            GPIO.output(led, 1)
            time.sleep(light_time)
            GPIO.output(led, 0)
        for led in reversed(leds):
            GPIO.output(led, 1)
            time.sleep(light_time)
            GPIO.output(led, 0)
