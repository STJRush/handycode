
# For LEDS marked GRY
# 
import machine
import utime
from machine import Pin

# flash time
t=1

led = Pin(25, Pin.OUT)

# flash the internal LED once
led.on()
utime.sleep(t)
led.off()
utime.sleep(t)

# This is defo how I wired them. Even though the yled on makes green. Weird.
gled = Pin(0, Pin.OUT)
rled = Pin(1, Pin.OUT)
yled = Pin(2, Pin.OUT)

def allOff():
    gled.off()
    rled.off()
    yled.off()

def orange(): # looks orange but similar to red
    rled.on()
    yled.on()

def red(): # looks red
    rled.on()

def green(): # looks green
    yled.on()

# TEST flash red then orange then green then off.
red()
utime.sleep(t)
allOff()
orange()
utime.sleep(t)
allOff()
green()
utime.sleep(t)
allOff()