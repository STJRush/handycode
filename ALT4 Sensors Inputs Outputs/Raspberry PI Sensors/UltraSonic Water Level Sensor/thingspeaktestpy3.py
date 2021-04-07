""" 
This Program sends a constant stream of sampleSensorReading (which is fixed to 50) up to Thingspeak to be graphed
""" 
import sys 
from time import sleep 
from urllib.request import urlopen

myAPI = "JDB150GBC7UT6MG2"  
# You need to change this to your own API Key for your channel. This one is my API key and will overwrite my channel.
# You must first make a channel on thingspeak. It'll then be under "API keys" tab as "Write API Key".


def updateThingSpeak(): 
   print('starting...') 
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI  

   while True: 
       try: 
            
           # you could change this sample reading to whatever you want eg. Temperature from a sensor, score from a game, this is what you edit.
           sampleSensorReading=50 
         
           # This part opens up a webpage and concatinates your reading onto the end of the URL.
           f = urlopen(baseURL + "&field1=%s" % (sampleSensorReading)) 
           print (f.read()) 
           f.close() 
            
           sleep(30) #uploads sensor values every 30 seconds
         
       except: 
           print('exiting.') 
           break

# runs the program here
updateThingSpeak()



"""
Wait a second... did you just update the graph by opening a URL with 
https://api.thingspeak.com/update?api_key=DA1K0TYF36CAE516&field1=20    ??

Is that all this does?

Could I technically just copy paste in the URL

https://api.thingspeak.com/update?api_key=JDB150GBC7UT6MG2&field1=42

into chrome to add 42 to your graph? 

Why yes you magnificant reader of instructions. Yes you can.

When you open that page, you'll even see the datapoint number you just sent.

"""
