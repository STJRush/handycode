# This program writes Temperature Data from the Picos interal thermometer to a CSV file

# Search on PYPI and install pico_zero from "Tools > Manage packages" in Thonny

from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine

temperature = pico_temp_sensor.temp
print(temperature)

# creates/reopens a csv file
myCSV = open("myCSVile.csv","a")

myCSV.write(str(temperature))
myCSV.write("\r\n")

myCSV.close()
