""" 
thingspeaktest
""" 
import sys 
import RPi.GPIO as GPIO 
from time import sleep 
import urllib2 


myAPI = "JDB150GBC7UT6MG7"


def main(): 
   print 'starting...' 
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 
   while True: 
       try: 
           xthing=10 
           f = urllib2.urlopen(baseURL + 
                               "&field1=%s" % (xthing)) 
           print f.read() 
           f.close() 
           sleep(50) #uploads DHT22 sensor values every 5 minutes 
       except: 
           print 'exiting.' 
           break 
# call main 
if __name__ == '__main__': 
   main()  
