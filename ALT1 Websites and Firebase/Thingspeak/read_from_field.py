# This program reads data from Thingspeak

import requests

# This is in the URL for your channel eg. https://thingspeak.com/channels/1379062
yourChannelNumber = 1379062

# This is the field that you want to read from (eg. Field 1 might be Temperature)
field = 1

# Goes off and finds the data
meThingData=requests.get("https://thingspeak.com/channels/"+str(1379062)+"/field/"+str(field))
meThingData=meThingData.json()['feeds'][-1]['field'+str(field)]

# Prints your data
print(meThingData)
