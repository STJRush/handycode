"""
This example will turn on ALL the LED's for 2 seconds
"""
import time
import pibrella

pibrella.light.red.on()
pibrella.light.yellow.on()
pibrella.light.green.on()
time.sleep(2)
pibrella.light.red.off()
pibrella.light.yellow.off()
pibrella.light.green.off()
time.sleep(2)
