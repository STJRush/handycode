from apds9960.const import *
from apds9960 import APDS9960

import smbus
from time import sleep

port = 1
bus2 = smbus.SMBus(port)
apds = APDS9960(bus2)

#sort of zeros the light sensor at the start
apds.enableLightSensor()


#takes six light values
for x in range(6):
    val = apds.readAmbientLight()
    print(val)
    sleep(1.3)
    
print("bye")

