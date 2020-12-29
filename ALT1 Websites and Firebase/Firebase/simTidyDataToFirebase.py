#sends a bunch of random fake temperatures to firebase

from firebase import firebase
import random
from time import sleep

firebase = firebase.FirebaseApplication('https://cookietest-a4f79.firebaseio.com', None)


for dataPointNumber in range(10): #repeat the code below 10 times

    simulated_temperature = random.randint(18,21)
    simulated_humidity = random.randint(55,59)

    #POSTS  to the database (POST means create an entry, does generate a nasty long node name)
    data = firebase.patch('/moOOARsimData/' , {'Reading' + str(dataPointNumber): simulated_temperature})
    
    sleep(1)
    print("Sent random temp to firebase", dataPointNumber+1 , " of 10")
    sleep(1)