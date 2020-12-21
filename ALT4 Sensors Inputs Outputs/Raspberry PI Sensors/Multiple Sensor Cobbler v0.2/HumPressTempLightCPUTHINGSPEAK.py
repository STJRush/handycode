import bme280
import smbus2
import smbus
from time import sleep
import sys  
from urllib.request import urlopen
import os


from apds9960.const import *
from apds9960 import APDS9960


port = 1
address = 0x77 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

#light stuff
bus2 = smbus.SMBus(port)
apds = APDS9960(bus2)

apds.enableLightSensor()


bme280.load_calibration_params(bus,address)

def readHumidity():
    bme280_data = bme280.sample(bus,address)
    humidity  = bme280_data.humidity
    print("Humidity:" , humidity)
    sleep(1)
    return humidity

def readPressure():
    bme280_data = bme280.sample(bus,address)
    pressure  = bme280_data.pressure
    print("Pressure: ", pressure)
    sleep(1)
    return pressure

def readTemperature():
    bme280_data = bme280.sample(bus,address)
    ambient_temperature = bme280_data.temperature
    print("Temp: " , ambient_temperature)
    sleep(1)
    return ambient_temperature

def readLight():
    lighting = apds.readAmbientLight()
    print("Light: " , lighting)
    sleep(1)
    return lighting


def measure_temp(): #cpu temps inside the pi
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))


def updateHumidity():    
    
    try:   
        f = urlopen(baseURL + "&field1=" +str(reading)) 
        #print (f.read()) 
        f.close() 
        sleep(600) #uploads sensor values every 5 minutes 
           
    except:
        print('exiting.') 

def updatePressure():    
    
    try:   
        f = urlopen(baseURL + "&field2=" +str(reading)) 
        #print (f.read()) 
        f.close() 
        sleep(600) #uploads sensor values every 5 minutes 
           
    except:
        print('exiting.') 

def updateTemperature():    
    
    try:   
        f = urlopen(baseURL + "&field3=" +str(reading)) 
        #print (f.read()) 
        f.close() 
        sleep(600) #uploads sensor values every 5 minutes 
           
    except:
        print('exiting.') 


def updateLight():    
    
    try:
        f = urlopen(baseURL + "&field4=" + str(reading))
        #print (f.read()) 
        f.close() 
        sleep(600) #uploads sensor values every 5 minutes
           
    except:
        print('exiting.') 


def updateCPUTemp():    
    
    try:
        f = urlopen(baseURL + "&field5=" + str(reading))
        #print (f.read()) 
        f.close() 
        sleep(600) #uploads sensor values every 5 minutes
           
    except:
        print('exiting.') 


myAPI = "K3Y5WNN2D6BI72J1"  #your key from your own thingspeak account. Put yours here.


print('starting...') 
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI  

while True:
    
    reading=readHumidity()
    updateHumidity()
    
    reading=readPressure()
    updatePressure()
    
    reading=readTemperature()
    updateTemperature()
    
    reading=readLight()
    updateLight()
    
    reading=measure_temp()
    updateCPUTemp()
    
    


