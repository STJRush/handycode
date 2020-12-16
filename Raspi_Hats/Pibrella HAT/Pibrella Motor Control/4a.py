"""
This example will turn on two motors for 8 seconds
"""
import time
import pibrella

pibrella.output.e.on()
time.sleep(8)
pibrella.output.e.off()
time.sleep(1)
