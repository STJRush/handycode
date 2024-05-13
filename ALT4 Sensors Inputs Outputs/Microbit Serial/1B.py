
import serial
import time

ser = serial.Serial()
ser.baudrate = 115200


ser.port = "COM9" 

print("Type CTRL + C to exit. (may take 5 seconds)")

ser.open()


while True:
    print("Starting to read")
    
    microbitData = str(ser.readline())
    print("Reading")
    print(microbitData)


    
    
    