import sys 
from urllib.request import urlopen

f = urlopen("https://api.thingspeak.com/update?api_key=DA1K0TYF36CAE516&field1=50")
#print(f.read())
f.close() 
