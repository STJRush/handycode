"""
This example will turn on the red LED for 2 seconds
"""
import time
import pibrella

pibrella.light.red.on()
time.sleep(2)
pibrella.light.red.off()
time.sleep(2)
