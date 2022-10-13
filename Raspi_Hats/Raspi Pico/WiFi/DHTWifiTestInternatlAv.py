# from https://www.freva.com/dht11-temperature-and-humidity-sensor-on-raspberry-pi-pico/ 
# but changed Pin 16 to pin 2 as no data getting there on GP16 (Expected 84 but got 0 pulses)
# maybe a Pico vs pico W thing
import machine
from machine import Pin
import utime
from dht import DHT11, InvalidChecksum
 
sensor = DHT11(Pin(2, Pin.OUT, Pin.PULL_DOWN))
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    print("Internal Temp:", round(temperature,2))
    
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
        print("Temperature: {}°C   Humidity: {:.0f}% ".format(temp, humidity))
        utime.sleep(2)
        
    except:
        print("Error, probably an InvalidPulseCount")
