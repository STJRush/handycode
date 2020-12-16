"""
This example will make the motor turn slowly
"""
import time
import pibrella

print ("Press Ctrl+C to stop")

while True:
    pibrella.output.e.on()
    time.sleep(0.01)
    pibrella.output.e.off()
    time.sleep(0.01)
