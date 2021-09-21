
import serial
import time

ser = serial.Serial()
ser.baudrate = 115200

# COM10 didn't work but COM12 did. So try COMwhateverYouSeeOnDeviceManager
ser.port = "COM3" 



print("Type CTRL + C to exit. (may take 5 seconds)")

ser.open()

try:
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
        
        # reads and cleans the second line from serial
        microbitdata = str(ser.readline()) 
        switch_position = microbitdata[2:]
        switch_position = switch_position.replace(" ","")
        switch_position = switch_position.replace("'","")
        switch_position = switch_position.replace("\\r\\n","")
        switch_position = int(switch_position)
        
        print(switch_position)
        
        # You could copy the code block above to read a third line etc.

except KeyboardInterrupt:
    print("\n Safely closing serial connection")
    ser.close()
    print("Done! Seeya later!")
    
    
    

