# https://www.i-programmer.info/programming/hardware/15148-the-pico-in-micropython-simple-input.html
from machine import Pin
import time
pin22In = Pin(22, Pin.IN,Pin.PULL_DOWN)
pin18In = Pin(18, Pin.IN,Pin.PULL_DOWN)

while True:
    if pin22In.value():
        print("22 ON")
    else:
        print("OFF")
        
    if pin18In.value():
        print("18 ON")
    else:
        print("OFF")
        
    time.sleep(0.5)
