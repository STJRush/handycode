# this should turn on the green light
# I had to get thonny to install micropython onto the pico, went for pico H
import machine
import utime
from machine import Pin

led = Pin(25, Pin.OUT)

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
 
while True:
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    temperature = str(temperature)
    
    first_digit = int(temperature[0])
    second_digit = int(temperature[1])
    
    lED_Flash_Duration = 0.2
    
    # flash to show first digit eg. 2 in 25C
    for i in range(first_digit):
        led.toggle()
        utime.sleep(lED_Flash_Duration)
        led.toggle()
        utime.sleep(lED_Flash_Duration)
    
    led.off()
    utime.sleep(2)
    
        # flash to show second digit eg. 5 in 25C
    for i in range(second_digit):
        led.toggle()
        utime.sleep(lED_Flash_Duration)
        led.toggle()
        utime.sleep(lED_Flash_Duration)
    
    utime.sleep(5)
    
    
