"""

This program streams DHT Temp and Humidity Data to Thingspeak.

The difference between this one and the other one in the folder is that this also
 - Collects 15 readings of Temp & Humidity in two lists and only uploads the most common reading (aka the "mode")
 - Does not upload anything when the sensor messes up and returns no value (Returns "None")
 
"""

import sys 
from time import sleep 
from urllib.request import urlopen
import Adafruit_DHT as DHT
import statistics


sleep(2)

myAPI = "DA1K0TYF36CAE516"  #your key from your own thingspeak account. Put yours here.



def updateThingSpeak(): 
   print('Updating thingspeak') 
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI  

   while True: 

           listyMcTemps = []
           listyMcHumids = []

           for x in range(15):

                # pre-sets these to zero in case the sensor fails to work and they break things later by being unassigned values
                temp = 0
                humid = 0

                # waits 5 secs before and after measurment to give that cheap sensor some time to work
                sleep(5)
                humid, temp = DHT.read_retry(DHT.DHT11, 4) #On GPIO Pin 4
                sleep(5)
                
                # debug print statment
                # print("Humidity is ", humid, "Temperature is ", temp)  


                if humid != None and temp !=None and humid != 0 and temp != 0 :     #this checks that neither read None
                  listyMcTemps.append(temp)
                  listyMcHumids.append(humid)
                
                else:
                   print("Ah craps, the sensor had a moment. Don't count that one!")
                   

                #  Yes, it's bad that there's a lot of try excepts below but DHT11 sensors are very hit and miss
                #  Also, I'm tired and can't come up with a proper if else
                
                try:
                  modeTemp = statistics.mode(listyMcTemps) # get the mode of the list
                except:
                  modeTemp = temp # if there is no unique mode, set it to the most recent value
                   
                try:
                  modeHumid = statistics.mode(listyMcHumids) # get the mode of the list
                except:
                  modeHumid = humid  # if there is no unique mode, set it to the most recent value


           print("Temperatures so far are...")
           print(listyMcTemps)

           print("The humidity values so far are...")
           print(listyMcHumids)

           print("Most common (mode) Temp in the last 15 readings is ", modeTemp)
           print("Most common (mode) Humidity in the last 15 readings is ", modeHumid)

           
           # uploads data to thingspeak here. You can change fields 1&2 to 3&4 if you've multiple sensors running.
           f = urlopen(baseURL + "&field1=%s" % (modeTemp) + "&field2=%s" % (modeHumid) ) 
           print ("Successfully uploaded data point ", f.read()) 
           f.close()
           
           print("Now waiting another 10 minutes before uploading more data to thingspeak...") 
           sleep(600) #uploads sensor values every 10 minutes
           print("")
                  
updateThingSpeak()

