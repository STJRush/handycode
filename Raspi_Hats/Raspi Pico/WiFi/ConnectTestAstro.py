# From tutorial at https://www.tomshardware.com/how-to/connect-raspberry-pi-pico-w-to-the-internet

import network
import secrets
import time
import urequests
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)
print(wlan.isconnected())
astronauts = urequests.get("http://api.open-notify.org/astros.json").json()
number = astronauts['number']
for i in range(number):
print(astronauts['people'][i]['name'])