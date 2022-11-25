import machine
import utime

# To test an Analogue GPIO Sensor:
# GND PIN is 3 down from the top right near USB
# +3V PIN is 5 down from the top right near USB
# ADC Analogue Pin is 7 down from the top right near USB
# GPIO DIAGRAM
# https://components101.com/sites/default/files/component_pin/Raspberry%20Pi-Pico-W-pinout.png

analog_value = machine.ADC(28)
 
while True:
    reading = analog_value.read_u16()     
    print("ADC: ",reading)
    utime.sleep(0.2)



