
import serial
from time import sleep

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM9"

ser.open()


# In fact... keep trying it! Again and again! MOAR!
while True:
        
        # First take in all the data and assign it to this variable
        microbitdata = str(ser.readline())
        
        # Get second bit onwards, call that signal_in
        signal_in = microbitdata[2:]
        
        # Remove any spaces
        signal_in = signal_in.replace(" ","")
        
        # Remove any apostrophies
        signal_in = signal_in.replace("'","")
        
        # Replace this with nothing (remove it)
        signal_in = signal_in.replace("\\r\\n","")
        

        
        # Print it to see if any of that rubbish above actually worked
        print(signal_in)
        
        # Take a break. You deserve it.
        sleep(3)

