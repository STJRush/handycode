"""
This example will turn on ALL the LED's for 2 seconds
It will then use while loop to repeat indefinetly
User types Ctrl C to exit
"""
import time
import pibrella

print ("Press Ctrl+C to stop")

while True:
    pibrella.light.red.on()
    time.sleep(2)
    pibrella.light.red.off()
    time.sleep(2)
