# from https://www.freva.com/dht11-temperature-and-humidity-sensor-on-raspberry-pi-pico/ 
# but changed Pin 16 to pin 2 as no data getting there on GP16 (Expected 84 but got 0 pulses)
# maybe a Pico vs pico W thing

from machine import Pin
import time
from dht import DHT11, InvalidChecksum
 
sensor = DHT11(Pin(2, Pin.OUT, Pin.PULL_DOWN))
 
while True:
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
        print("Temperature: {}°C   Humidity: {:.0f}% ".format(temp, humidity))
        time.sleep(2)
        
    except:
        print("Error, probably an InvalidPulseCount")
