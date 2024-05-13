
import serial
import time

ser = serial.Serial()
ser.baudrate = 115200

# COM10 didn't work but COM12 did. So try COMwhateverYouSeeOnDeviceManager
ser.port = "COM3" 

print("Type CTRL + C to exit. (may take 5 seconds)")

ser.open()


while True:
    
    print("Starting to read")
    
    # reads and cleans the first line from serial (temp)
    microbitdata = str(ser.readline())
    temperature = microbitdata[2:]
    temperature = temperature.replace(" ","")
    temperature = temperature.replace("'","")
    temperature = temperature.replace("\\r\\n","")
    temperature = int(temperature)
    
    print(temperature)
        
    

