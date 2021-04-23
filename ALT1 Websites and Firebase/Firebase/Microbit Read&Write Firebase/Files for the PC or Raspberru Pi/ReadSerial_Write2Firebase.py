# Got teh micro:bit serial code from Pauric O'Donnell, this video: https://youtu.be/fzMVV7ZMyvE
# Thanks Pauric!

import serial
from firebase import firebase
import random
from time import sleep
from datetime import datetime,date, timedelta

firebase = firebase.FirebaseApplication('https://cookietest-a4f79.firebaseio.com', None)



ser = serial.Serial()
ser.baudrate = 115200

# find the port by typing device manager into the start menu and looking under ports. It's one of those few listed.
ser.port = "COM12"

print("Type CTRL + C to exit. (may take 5 seconds)")

ser.open()

try:
    while True:
        
        now = datetime.now() #gets the date & time from your computer right now
        
        microbitdata = str(ser.readline())
        temperature = microbitdata[2:]
        temperature = temperature.replace(" ","")
        temperature = temperature.replace("'","")
        temperature = temperature.replace("\\r\\n","")
        temperature = int(temperature)
        
        print(temperature)
        
        data = firebase.patch('/microbitSerialTemps/' , {now.strftime("%H:%M:%S"): temperature})
        print(data)
        sleep(3)


except KeyboardInterrupt:
    print("\n Safely closing serial connection")
    ser.close()
    print("Done! Seeya later!")
    
    
    
