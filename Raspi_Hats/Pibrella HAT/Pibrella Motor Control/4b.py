"""
This example will turn on one motor for 4 seconds and loop the cycle
"""
import time
import pibrella

while True:
    pibrella.output.e.on()
    time.sleep(4)
    pibrella.output.e.off()
    time.sleep(1)
