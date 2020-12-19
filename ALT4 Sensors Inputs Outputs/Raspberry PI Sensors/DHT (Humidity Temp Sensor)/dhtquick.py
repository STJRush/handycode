import Adafruit_DHT as DHT

humid, temp = DHT.read_retry(DHT.DHT11, 4)

print(temp, humid)

