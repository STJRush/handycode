# Sim mode allows you to test your project when a microbit is not connected

# Set the simMode  boolean variable to 1 to simulate values and back to 0 to read from Microbit
simMode = 1

import serial
import time
from random import randint


def readSerial():
    
    # reads and cleans the first line from serial (temp)
    microbitdata = str(ser.readline())
    temperature = microbitdata[2:]
    temperature = temperature.replace(" ","")
    temperature = temperature.replace("'","")
    temperature = temperature.replace("\\r\\n","")
    temperature = int(temperature)
    print("Recorded Temp from Micro:bit:", temperature)
    
    return temperature


def getSimValue():
    simtemperature = randint(1,20)
    print("Simluated a Temperature",simtemperature)
    
    return simtemperature


# Create empty list to store data later
dataList =[]




if simMode == 0:
    # setup microbit serial
    ser = serial.Serial()
    ser.baudrate = 115200

    # COM10 didn't work but COM12 did. So try COMwhateverYouSeeOnDeviceManager
    ser.port = "COM35" 
    ser.open()


# record 10 values
for x in range(10): 

    if simMode == 1:
        
        data = getSimValue()
    
    elif simMode == 0:
        
        data = readSerial()
        
    dataList.append(data)
    

print("Temperature is", dataList)

        
    

