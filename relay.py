import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P8_13", GPIO.OUT)
GPIO.setup("P8_14", GPIO.OUT)

raw_input("High")
GPIO.output("P8_13", GPIO.HIGH)
GPIO.output("P8_14", GPIO.LOW)

raw_input("Low")
GPIO.output("P8_13", GPIO.LOW)
GPIO.output("P8_14", GPIO.HIGH)

GPIO.cleanup()
