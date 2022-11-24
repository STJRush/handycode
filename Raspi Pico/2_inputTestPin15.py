from machine import Pin
import time
led = Pin("LED", machine.Pin.OUT)
led.off()
time.sleep(2)
pinIn = Pin(15, Pin.IN,Pin.PULL_UP)

for i in range(200):
    if pinIn.value():
        led.on()
    else:
        led.off()
    time.sleep(0.1)
    
print("done")


for x in range(4):
    led.on()
    time.sleep(0.1)
    led.off()
    time.sleep(0.1)
