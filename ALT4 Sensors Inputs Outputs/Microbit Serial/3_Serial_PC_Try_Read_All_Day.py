# This version has lots of try excepts to handle errors over longer period of time
# This program takes a variable (signal_in here but could be any serial data) from a microbit and brings it into Thonny. 
# USB Serial data comes with lots of junk text like \\r\\n so most of this program is for cleaning those parts away leaving just the variable we want.

import serial
from time import sleep

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM23"

print("Type CTRL + C to exit. (may take 5 seconds)")

# Opens the packet of crunchie nut cornflakes
ser.open()

# Try this unless you hit CTL+C
try:
    
    # In fact... keep trying it! Again and again! MOAR!
    while True:
        
        # Try read the serial data
        try:
            
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
        
        # Except don't try read blank numbers. Pass them by.
        except ValueError:
            pass

except KeyboardInterrupt:
    
    # https://www.youtube.com/watch?v=AxcM3nCsglA
    print("\n HE DID THE MASH! ... He did the CTRL+C mash")
    ser.close()
    print("The keyboard mash!")
    

# Don't forget you can show the show plotter on Thonny under "View"
