# Code derived from STJHandycode, original credit to Pauric O'Donnell on YT
# Modified by 18LKennedy
# Tested on an 2017 iMac (the one with USB A ports)

# THIS CODE IS FOR MAC USAGE ONLY (Might apply to Linux)

import serial
import time

# Instructions:
# Open Terminal,
# Type: ls /dev/cu.* ,
# Look for usbmodem, whatever that is,
# Copy /dev/cu.usbmodem[NUMBERS] and replace it as your COM port.
# Keep the budrate at 115200
# It should read, if it doesnt, you're on your own

ser = serial.Serial('/dev/cu.usbmodem14302')
ser.baudrate = 115200
ser.port = "/dev/cu.usbmodem14302" 



print("Type Control + C (Not Command + C) to exit. (may take 5 seconds)")

# If an error "The port is open" occures, remove ser.open()

#ser.open()

try:
    while True:
        print("Starting to read")
        
        microbitData = str(ser.readline())
        print("Reading")
        print(microbitData)

except KeyboardInterrupt:
    print("\n Safely closing serial connection")
    ser.close()
    print("Done! Seeya later!")