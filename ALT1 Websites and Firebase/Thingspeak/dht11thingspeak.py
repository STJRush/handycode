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

                temp = 0
                humid = 0

               
                sleep(5)
                humid, temp = DHT.read_retry(DHT.DHT11, 4) #On GPIO Pin 4
                sleep(5)
                # print("Humidity is ", humid, "Temperature is ", temp)


                if humid != None and temp !=None and humid != 0 and temp != 0 :     #this checks that niether read None
                  listyMcTemps.append(temp)
                  listyMcHumids.append(humid)
                  # print("Cool. Added that to the list")
                
                else:
                   print("Ah craps, the sensor had a moment. Don't count that one!")
                   

                #  Yes, it's bad that there's a lot of try except below but DHT11 sensors are very hit and miss
                #  Also, I'm tired. 
                
                try:

                  modeTemp = statistics.mode(listyMcTemps)

                except:
                  modeTemp = temp

                   
                try:

                  modeHumid = statistics.mode(listyMcHumids)

                except:
                  modeHumid = humid


           print("Temperatures so far are...")
           print(listyMcTemps)

           print("The humid values so far are...")
           print(listyMcHumids)

           print("Most common (mode) Temp in the last 15 readings is ", modeTemp)
           print("Most common (mode) Humidity in the last 15 readings is ", modeHumid)

           
           # uploads data to thingspeak here. You can change fields 1&2 to 3&4 if you've multiple sensors running.
           f = urlopen(baseURL + "&field1=%s" % (modeTemp) + "&field2=%s" % (modeHumid) ) 
           print (f.read()) 
           f.close()
           
           print('Will wait another 10 minutes before uploading more data to thingspeak...") 
           sleep(600) #uploads sensor values every 10 minutes
          
                  
updateThingSpeak()

