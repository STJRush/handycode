# thingspeak can accept strings but it's a little hard to show them.
# Firebase is best for sending strings to a webpage.

import sys 
from time import sleep 
from urllib.request import urlopen


myAPI = "JDB150GBC7UT6MG7"  #your key from your own thingspeak account. Put yours here.

def updateThingSpeak(): 
   print('Now updating thingspeak') 
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI    

   f = urlopen(baseURL + "&field1=%s" % ("Danny") + "&field2=%s" % (highScore) ) 
   print ("Success! I uploaded data point No. ", f.read())
   f.close()

# Program Starts Here

playerName = "Danny"
highScore = -3

updateThingSpeak()



