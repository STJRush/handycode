# this should turn on the green light
# I had to get thonny to install micropython onto the pico, went for pico H
import machine
import utime
from machine import Pin

# followed tutorial at https://www.tomshardware.com/how-to/oled-display-raspberry-pi-pico
# installed micropython-ssd1306
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

oled = SSD1306_I2C(128, 32, i2c) # set you oled size, mine was 128 pixels x 32 pixels
"""
oled.text("HI DANNY", 0, 0)
oled.hline(2,31,120,1)
oled.show()
"""



# internal led
led = Pin(25, Pin.OUT)
led.on()
utime.sleep(0.1)
led.off()

rled = Pin(2, Pin.OUT)
gled = Pin(3, Pin.OUT)
bled = Pin(4, Pin.OUT)



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

def purple():
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
        utime.sleep(0.1)
        rled.off()
        utime.sleep(0.1)
    utime.sleep(3)

def redFlashyForever():
    rled.on()
    utime.sleep(0.3)
    rled.off()
    utime.sleep(0.3)  
    
def blueTripleFlashy():
    for x in range(3):
        bled.on()
        utime.sleep(0.1)
        bled.off()
        utime.sleep(0.1)
    utime.sleep(3)

def blueFlashyForever():
    bled.on()
    utime.sleep(0.3)
    bled.off()
    utime.sleep(0.3)


sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    oled.fill(0)
    
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    temperature=round(temperature,2)
    print(temperature)
    
    oled.text(("Temp:"+str(temperature)+"C"), 0, 0)
    oled.show()
    
    
    #temperature = str(temperature)
    #lED_Flash_Duration = 0.2
    
    #reset light colour
    lightsOut()
    if temperature < 14 :                        # Frickin freeeezin
        blueFlashyForever()
        print("Blue Flash")
    elif temperature >= 14 and temperature < 16: # Way too cold
        blueTripleFlashy()
        print("Blue Triple Flash")
    elif temperature >= 16 and temperature < 18: # Too cold
        blue()
        print("Blue")
    elif temperature >= 18 and temperature < 20: # Not great, not terrible.
        blueGreen()
        print("Blue Green")
    elif temperature >= 20 and temperature < 22: # NICE
        green()
        print("Green")
    elif temperature >= 22 and temperature < 24: # Nice but a tad warm
        greenOrange()
        print("Green Orange")
    elif temperature >= 24 and temperature < 26: # Almost too warm
        red()
        print("Red")
    elif temperature >= 26 and temperature < 28: # Too hot
        redTripleFlashy()
        print("Red Triple Flash")
    elif temperature >= 28:
        redFlashyForever()                       # Melting my feet
        print("Continuous Red Flash")
        
    # check program every 10 seconds
    utime.sleep(10)

    

