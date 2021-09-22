
import serial
import sys 
from time import sleep 
from urllib.request import urlopen

# <<< YOU NEED TO CHANGE THIS BIT! >>>
myAPI = "0P838AQUU1O7B3EJ"  #your key from your own thingspeak account. Put yours here.


# the thingspeak bit
def updateThingSpeak(): 
   print('Now updating thingspeak') 
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI    

   f = urlopen(baseURL + "&field1=%s" % (temperature) + "&field2=%s" % (switch_position) ) 
   print ("Success! I uploaded data point No. ", f.read())
   f.close()

# the bit that reads the serial from the microbit
ser = serial.Serial()
ser.baudrate = 115200


# <<< YOU NEED TO CHANGE THIS BIT! >>>
# Try COM...ah...whateverYouSeeOnDeviceManager under ports. Type Device Manager in the start menu.
ser.port = "COM3" 


print("Type CTRL + C to exit. (may take 5 seconds)")
ser.open()

try:
    while True:
        print("Reading Serial Data and Switch position (1 or 0)")
        
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
        
        # Updates Thingspeak
        updateThingSpeak()

except KeyboardInterrupt:
    print("\n Safely closing serial connection")
    ser.close()
    print("Done! Seeya later!")
    
    
    


