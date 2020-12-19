import Adafruit_DHT as DHT

sensor = DHT.DHT11
pin = 4

humidity, temperature = DHT.read(sensor, pin)

print(humidity)
print(temperature)