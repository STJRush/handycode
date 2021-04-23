from firebase import firebase
import random
from time import sleep

firebase = firebase.FirebaseApplication('https://cookietest-a4f79.firebaseio.com', None)


for demHours in range(8): # repeat the code below 8 times representing 8 hours

    simulated_people = random.randint(0,30)  # makes up a random number of people

    # attatches names to the data
    data = {"NumOfPeople": simulated_people, "Hour": demHours}
    
    # It's (demHours + 1) because otherwise there'd be a data point called Hour 0. ZeroHour sounds cool. But no.
    data = firebase.patch('/someRandoSimPeopleNumbers/' , {'Hour ' + str(demHours+1): simulated_people})
    
    sleep(1)
    print("Sent random temp to firebase", demHours+1 , " of 8")
    sleep(1)
    
"""
Expected Output in Realtime Database:
    
    someRandoSimPeopleNumbers
        Hour 1: 18
        Hour 2: 8
        Hour 3: 17
        Hour 4: 27
        Hour 5: 19
        Hour 6: 16
        Hour 7: 18
        Hour 8: 27

    
    
"""
