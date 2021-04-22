# Got most of this code from Pauric O'Donnell, this video: https://youtu.be/fzMVV7ZMyvE
# Use this code to test your COM ports. This version does not clean the input. Next one does.
# Thanks Pauric!

import serial
import time

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM12"

print("Type CTRL + C to exit. (may take 5 seconds)")

ser.open()

try:
    while True:
        microbitdata = str(ser.readline())
        temperature = microbitdata[2:]
        temperature = temperature.replace(" ","")
        temperature = temperature.replace("'","")
        temperature = temperature.replace("\\r\\n","")
        temperature = int(temperature)
        
        print(temperature)
        
        time.sleep(3)


except KeyboardInterrupt:
    print("\n Safely closing serial connection")
    ser.close()
    print("Done! Seeya later!")
    
    
    
