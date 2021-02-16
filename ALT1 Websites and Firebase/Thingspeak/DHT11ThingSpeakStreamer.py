import sys 
from time import sleep 
from urllib.request import urlopen
import Adafruit_DHT as DHT


myAPI = "DA1K0TYF36CAE516"  #your key from your own thingspeak account. Put yours here.



def updateThingSpeak(): 
   print('Updating thingspeak') 
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI  

   while True: 
       try:
           
           humid, temp = DHT.read_retry(DHT.DHT11, 4) #On GPIO Pin 4
           print("Humidity is ", humid, "Temperature is ", temp) 
            
           f = urlopen(baseURL + "&field1=%s" % (temp) + "&field2=%s" % (humid) ) 
           print (f.read()) 
           f.close() 
           sleep(10) #uploads sensor values every 5 minutes
          

           humid, temp = DHT.read_retry(DHT11, 4) 
           f = urlopen(baseURL + "&field3=%s" % (humid)) 
           print (f.read()) 
           f.close() 
           sleep(10)
           
       except: 
           print('Ooops... lets try again...') 
           
updateThingSpeak()



