# https://www.i-programmer.info/programming/hardware/15148-the-pico-in-micropython-simple-input.html
from machine import Pin
import time
pinIn = Pin(22, Pin.IN,Pin.PULL_UP)
pinLED = Pin(25, Pin.OUT)
while True:
    if pinIn.value():
        pinLED.on()
    else:
        pinLED.off()
    time.sleep(0.5)
