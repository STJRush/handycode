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

           
            
           f = urlopen(baseURL + "&field1=%s" % (modeTemp) + "&field2=%s" % (modeHumid) ) 
           print (f.read()) 
           f.close() 
           sleep(600) #uploads sensor values every 10 minutes
          
           

           print('Ooops... lets try again...') 
           
updateThingSpeak()

