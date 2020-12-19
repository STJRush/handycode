import Adafruit_DHT as DHT
from time import sleep
from firebase import firebase


#API KEY
firebase = firebase.FirebaseApplication('https://rpitempdata.firebaseio.com', None)

while True:
    humid, temp = DHT.read_retry(DHT.DHT11, 4)

    print("Let's start with getting python to read from the sensor..")
    print("humidity is", humid)
    print("temperature is", temp)

    #####


    print("Now let's upload that to Firebase")
    #Patches on extra data from our temp and humidity variables at the top of the program, simulated sensor readings
    result = firebase.patch('/sensor/dht/', {'Temperature': temp, 'Humidity': humid})

    sleep(2)
    print("Give it a moment to upload...")
    sleep(2)

    print("Okay Done")
    print("Now seeing if we can read from the database...")

    print("The last uploaded temperature was:")
    result = firebase.get('/sensor/dht/Temperature', None)
    print(result)

    print("The last uploaded humidity was:")
    result = firebase.get('/sensor/dht/Humidity', None)
    print(result)

    sleep(3)
    print("program done")

    sleep(1000)

