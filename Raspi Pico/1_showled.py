# this should turn on the green light
# I had to get thonny to install micropython onto the pico, went for pico H

from machine import Pin
led = Pin(25, Pin.OUT)

led.toggle()
