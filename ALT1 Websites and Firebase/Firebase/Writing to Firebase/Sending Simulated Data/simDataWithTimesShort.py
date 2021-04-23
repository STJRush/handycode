from firebase import firebase
import random
from time import sleep
from datetime import datetime

firebase = firebase.FirebaseApplication('https://cookietest-a4f79.firebaseio.com', None)

for count in range(10): # repeat the code below 10 times representing 10 seconds

    simulated_people = random.randint(1,30)  # makes up a random number of people 1-30
    
    now = datetime.now() #gets the date & time from your computer right now each time
    
    # patches to firebase Name (time right now) : The value being random number from 1-30
    data = firebase.patch('/myData/' , {now.strftime("%H:%M:%S") : simulated_people})

    print("We just uploaded", data)

    sleep(1) # waits 1 second before uploading again
