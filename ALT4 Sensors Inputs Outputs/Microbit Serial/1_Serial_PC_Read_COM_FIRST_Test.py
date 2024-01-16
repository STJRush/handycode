# Got most of this code from Pauric O'Donnell, this video: https://youtu.be/fzMVV7ZMyvE
# Use this code to test your COM ports. This version does not clean the input. Next one does.
# Thanks Pauric!

import serial
import time

ser = serial.Serial()
ser.baudrate = 115200


# This is the fiddly bit, finding the COM port for your own microbit.
# I typed chgport in commandline like in Pauric's video but had no luck :(
# I eventually found the correct port by opening device manager in windows.
# Open the start menu and type device manager.
# In device manager under ports, COM10 and COM12 were listed. No others.
# So it was like that Monty Python video where Mr. Evee Lambert is hiding behind one of three
# bushes in an open field. They just fire an artillary shell at all three.
# So seeing as python gets it's name from Monty Python, that's what I did. I tried each one.
# COM10 didn't work but COM12 did. So try COMwhateverYouSeeOnDeviceManager
ser.port = "COM9" 



print("Type CTRL + C to exit. (may take 5 seconds)")

ser.open()

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
    
    
    