#For testing if GPIOs are working
#Godspeed.

import RPi.GPIO as GPIO   #lets you use GPIO
from time import sleep    #lets you use sleep(2) as a timer for the lights

GPIO.setmode(GPIO.BCM)    #tells the program what labeling system to use

GPIO.setup(23, GPIO.OUT)  #tells the pi exactly what number pin you'll be using
GPIO.setup(24, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

print("Welcome to the Murray GPIO Test")
print("Testing GPIOs 21,24,17,27 in order.")
sleep(0.5)


print("GPIOTEST23 ON")
GPIO.output(23, GPIO.HIGH)     #tells the pi to turn on this pin
sleep(1)
print("GPIOTEST23 OFF")        #waits 2 seconds
GPIO.output(23, GPIO.LOW)      #tells the pi to turn off this pin

sleep(0.5)

print("GPIOTEST24 ON")
GPIO.output(24, GPIO.HIGH)    #tells the pi to turn on this pin
sleep(1)                      #waits 2 seconds
print("GPIOTEST24 OFF")
GPIO.output(24, GPIO.LOW)

sleep(0.5)

print("GPIOTEST17 ON")
GPIO.output(17, GPIO.HIGH)
sleep(1)
print("GPIOTEST17 OFF")
GPIO.output(17, GPIO.LOW)

sleep(0.5)

print("GPIOTEST27 ON")
GPIO.output(27, GPIO.HIGH)
sleep(1)
print("GPIOTEST27 OFF")
GPIO.output(27, GPIO.LOW)

sleep(0.5)

#the cleanup

GPIO.cleanup()             #shuts down all GPIO stuff
