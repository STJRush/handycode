#Cookie meter firebase sample code
#You must have the HX711 python file in the same folder as this code uses that!


import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711


#firebase is such a cool name. If you don't agree, hold ALT and mash F4 on the keyboard right now.
from firebase import firebase  


#Below is where you type the address of your Firebase
firebase = firebase.FirebaseApplication('https://cookietest-a4f79.firebaseio.com', None)

#This function just cleans up when everything is done.
def cleanAndExit():
    print "Cleaning..."
    GPIO.cleanup()
    print "Bye!"
    sys.exit()

#Using GPIO 5,6 for the scale.
hx = HX711(5, 6)
hx.set_reading_format("LSB", "MSB")
hx.set_reference_unit(412)

hx.reset()
hx.tare()


print("Welcome to Mr. Murray's Cookie Scale")

print(" me no care   (.)(*)            ")
print("       ...   / ___, \  .-.      ")
print("       .-. _ \ '--' / (:::)     ")
print("      (:::{ \-`--=-`-/ }^       ")
print("       `-' ` /      \ `         ")
print("             \      /           ")
print(" long as    _/  /\  \_          ")
print(" me get    {   /  \   }         ")
print(" cookie     `-`    `-`           ")


while True:
    
    try:
        
        val = hx.get_weight(5)
        print (str(val)+"g worth of delicious cookie detected")
        

        hx.power_down()
        hx.power_up()
        time.sleep(0.5)   #this pause can be bigger if you're having errors


        print("Sending cookie numbers to firebase")

        cookieNum = val/42   # eg. hmmmm...me thinks this means fifty delicious cookie. 42g per cookie.


        # the code below sends the value of "cookieNum" taken from the sensor to Firebase
        # My realtime database has the tree /cookieMeter/Number_of_cookies
        # This will write over Number_of_cookies with whatever the sensor says divided by 42 aka cookieNum
        
        
        #                         location          write over this     with this
        result = firebase.patch('/cookieMeter/', {'Number_of_cookies': cookieNum})
    


        #reads the database to see if it's updated (takes 10 seconds)
        result = firebase.get('/cookieMeter', None)
        print("Me see that firebase has..")
        print(result)
        print("Delicious....scrumcious....coookies")
        time.sleep(4)
        
        
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()

