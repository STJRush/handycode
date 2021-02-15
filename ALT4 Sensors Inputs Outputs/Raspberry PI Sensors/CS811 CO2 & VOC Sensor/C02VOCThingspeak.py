# This example reads and prints CO2 equiv. measurement, TVOC measurement, and temp every 2 seconds
# Sensor works best after "running in" for 10-20 mins.


import sys 
from urllib.request import urlopen

from time import sleep
from Adafruit_CCS811 import Adafruit_CCS811



myAPI = "DA1K0TYF36CAE516"  #your key from your own thingspeak account. Put yours here.

print('Updating thingspeak') 
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI  

while True:
    
    try:

        ccs =  Adafruit_CCS811()

        while not ccs.available():
            pass
        temp = ccs.calculateTemperature()
        ccs.tempOffset = temp - 25.0


        ccs.tempOffset = temp - 25.0


        if ccs.available():
            temp = ccs.calculateTemperature()
            if not ccs.readData():
              print ("CO2: ", ccs.geteCO2(), "ppm, TVOC: ", ccs.getTVOC(), " temp: ", temp)
            
            else:
              print ("ERROR!")
              while(1):
                pass
        sleep(2)


        f = urlopen(baseURL + "&field3=%s" % (ccs.geteCO2()) + "&field4=%s" % (ccs.getTVOC())+ "&field5=%s" % (temp)) 
        print (f.read()) 
        f.close() 
        sleep(300)


    except:
        print("Ooops..something went wrong..let's try again!")






        """
        What are safe levels of CO and CO2 in rooms?

        CO2 (Carbon Dioxide)
        250-400ppm  Normal background concentration in outdoor ambient air
        400-1,000ppm    Concentrations typical of occupied indoor spaces with good air exchange
        1,000-2,000ppm  Complaints of drowsiness and poor air.
        2,000-5,000 ppm Headaches, sleepiness and stagnant, stale, stuffy air. Poor concentration, loss of attention, increased heart rate and slight nausea may also be present.
        5,000   Workplace exposure limit (as 8-hour TWA) in most jurisdictions.
        >40,000 ppm Exposure may lead to serious oxygen deprivation resulting in permanent brain damage, coma, even death.

        CO (Carbon Monoxide)
        9 ppm   CO Max prolonged exposure (ASHRAE standard)
        35 ppm  CO Max exposure for 8 hour work day (OSHA)
        800 ppm CO Death within 2 to 3 hours
        12,800 ppm  CO Death within 1 to 3 minutes

        VOC (Volatile Organic Compounds #smelly things #don't breath these in)
        VOCs such as Alcohol, Formaldehyde, Smog, Acetone, Pesticides can be detected but the sensor won't tell you which.
        You need to calibrate this yourself.
        INFO on VOCs:
        https://foobot.io/guides/list-of-all-volatile-organic-compounds.php

        """
