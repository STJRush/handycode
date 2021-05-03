"""
This program uploads two fake variables to ThingSpeak every 20 seconds.
1. Get this program to run correctly
2. Try it with your own Thingspeak Channel
3. On a Raspberry Pi, try streaming the current CPU Temperature. You can find this code here:
https://raw.githubusercontent.com/STJRush/handycode/master/ALT4%20Sensors%20Inputs%20Outputs/Raspberry%20PI%20Sensors/CPU_Temperature_Measure_Simple.py

On the free version of ThingSpeak you can only send data every 15 seconds.

"""

import sys 
from time import sleep 
from urllib.request import urlopen


myAPI = "DA1K0TYF36CAE516"  #your key from your own thingspeak account. Put yours here.

def updateThingSpeak(): 
   print('Now updating thingspeak') 
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI    

   f = urlopen(baseURL + "&field1=%s" % (fakeTemperatureMeasurement) + "&field2=%s" % (fakeHumidityMeasurement) ) 
   print ("Success! I uploaded data point No. ", f.read())
   f.close()

# Program Starts Here

fakeTemperatureMeasurement = 42
fakeHumidityMeasurement = 99

while True:
    updateThingSpeak()
    print("Now waiting another 20 seconds before uploading more data to thingspeak...") 
    sleep(20)
    print("")


