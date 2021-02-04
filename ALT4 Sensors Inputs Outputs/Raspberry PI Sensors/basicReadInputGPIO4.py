# Generic Reed'n dem inputs (GPIO 4) 

import RPi.GPIO as GPIO  
from time import sleep    # For pausing
GPIO.setmode(GPIO.BCM)    # BCM numbering, not BOARD
GPIO.setup(4, GPIO.IN)    # Sets pin4 to an input 


try:                      # Doesn't kill the program on an error, goes to finally instead
    while True:           # MASH CTRL+C to stop the program
        
        if GPIO.input(4): # Checks what's up with Pin 4, if it's TRUE or FALSE
            print("I'm reading TRUE on GPIO 4")
            
        else:  
            print("I'm reading FALSE on GPIO 4") 

        sleep(1)          # Wait 1 second before the next reading  
  
finally:                  # When you CTL+C out of the try block, you end up here
    
    print("Cleaning up...")
    GPIO.cleanup()        # Turns off all pins that are still on so the next program runs cleanly
    
    
    
    
"""
    Raspberry Pi
    
    Wiring Diagram
   _______________
   !  sd card o+ !     + = 5V
   !          oo !     - = GND
   !          o- ! 
   !          4o !     4 = GPIO 4
   !          oo !     
   !          oo !
   !HDMI      oo !
   !          oo !
   !          oo !
   !          oo !
   !          oo !
   !          oo !
   !             !
   !             !
   !___   ___ ___!
   !eth   usb usb!
   !___   ___ ___!

Watch out! Many sensors read TRUE when they don't detect something
and FALSE when they do. It's weird...but aren't we all a bit weird :)

I mean all batteries are technically labelled backwards. Does that
kind of make this a double negative and therefore correct? Do our
own nerves in our fingers work in the same way? Can nerves be used
as both inputs and outputs like GPIO? Who invented the tent? Probably
a cave person hiding under some skins I guess. But is that not more of
a blanket? A tent needs a pole doesn't it? Like maybe they used a stick?
I'll bet it was accidental. I'll bet one caveperson had a big flipin
stick and went in to hit someone and then it got stuck under the
blanket of animal skins and they two of them were sitting there thinking
hey...this is nice. Simpler times perhalps. I bet you starting a
fire was just as frustrating as getting sensors to work. Same sh1t.
Different milenia. I once saw someone throw an iPhone at a spider.
What do you think a caveman would think of that? Oh look there's a hand
held digital doorway to the sum of all human knowledge and that human is
about to throw it at some poor creature the size of a grain of rice.
Imagine the sh1t people will throw at spiders 200 years from now...
Things so fantastical that you can't even imagine. From the spider's
point of view, very little has changed over the last ten thousand years.
A rock, shoe, a phone and an personal teleporter are best avoided.
Humans will always be a bit weird. So let's not complain about sensors
reading FALSE when they TRUELY detect something.

They're TRUELY far less weird that you are.

"""
    