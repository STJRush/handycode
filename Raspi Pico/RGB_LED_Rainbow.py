# This code is for a white RGB LED that I've soldered a small resistor to the GND leg onto
# On this LED, Blue+Red (purple) wasn't working so have removed it from the code
# Maybe my LED was bad

import machine
import utime
from machine import Pin

# internal led
led = Pin(25, Pin.OUT)
led.on()

"""

    RGB LED Wiring Diagram
       _______
      |    ¬  |
      |       |
      |_______|
     /  |   |  \
    /   |   |   \
    |   |   |   |
    |   |   |   |
    |   |   |   |
    |   |   |   |
    R   |   G   B
        GND
  
Pins on the pico
   GP2  G  GP1 GP0  
    |   |   |   |
"""
# THIS BIT I CHANGED FOR THE PIXEL
rled = Pin(2, Pin.OUT)
gled = Pin(1, Pin.OUT)
bled = Pin(0, Pin.OUT)

def lightsOut():
    rled.off()
    gled.off()
    bled.off()

def red():
    rled.on()

def green():
    gled.on()

def blue():
    bled.on()

def purple(): # looked just red?
    rled.on()
    bled.on()


def blueGreen():
    gled.on()
    bled.on()

def greenOrange():
    gled.on()
    rled.on()
    
def redTripleFlashy():
    for x in range(3):
        rled.on()
        utime.sleep(0.2)
        rled.off()
        utime.sleep(0.2)
        
def redFlashyForever():
    rled.on()
    utime.sleep(0.2)
    rled.off()
    utime.sleep(0.2)  
    
def blueTripleFlashy():
    for x in range(3):
        bled.on()
        utime.sleep(0.2)
        bled.off()
        utime.sleep(0.2)


def blueFlashyForever():
    bled.on()
    utime.sleep(0.3)
    bled.off()
    utime.sleep(0.3)

# Program starts here:

red()
utime.sleep(0.8)
lightsOut()

purple()
utime.sleep(0.8)
lightsOut()

green()
utime.sleep(0.8)
lightsOut()

blueGreen()
utime.sleep(0.8)
lightsOut()

blue()
utime.sleep(0.8)
lightsOut()

blueTripleFlashy()
redTripleFlashy()