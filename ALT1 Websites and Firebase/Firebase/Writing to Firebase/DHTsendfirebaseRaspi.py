







import sys 
from time import sleep 
from urllib.request import urlopen
import Adafruit_DHT as DHT


myAPI = "JDB150GBC7UT6MG7"  #your key from your own thingspeak account. Put yours here.


def updateThingSpeak(): 
   print('starting...') 
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI  

   while True: 
       try: 
           sampleSensorReading=50 
           f = urlopen(baseURL + "&field1=%s" % (sampleSensorReading)) 
           print (f.read()) 
           f.close() 
           sleep(50) #uploads sensor values every 5 minutes 
       except: 
           print('exiting.') 
           break

updateThingSpeak()


while True:
    humid, temp = DHT.read_retry(DHT.DHT11, 4) #On GPIO Pin 4

    print("Let's start with getting python to read from the sensor..")
    print("humidity is", humid)
    print("temperature is", temp)

    

