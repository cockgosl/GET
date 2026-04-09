import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

bit_c = 12

leds = [16, 12, 25, 17, 27, 23, 22, 24]

GPIO.setup(leds, GPIO.OUT)

GPIO.setup(leds, 0)

num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

up = 9
down = 10

GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)

while True:
    if GPIO.input(up):
        if num < 255:
            num = num+1
        GPIO.output(leds, dec2bin(num))
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(down):
        if num > 0:
            num -= 1
        GPIO.output(leds, dec2bin(num))
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(up) & GPIO.input(down) :
        num = 255
        GPIO.output(leds, dec2bin(num))
        print(num, dec2bin(num))
        time.sleep(sleep_time)