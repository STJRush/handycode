import Adafruit_DHT as DHT

humid, temp = DHT.read(DHT.DHT11, 4)

print(humid, temp)

print(temp)