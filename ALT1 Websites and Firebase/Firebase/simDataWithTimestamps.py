from firebase import firebase
import random
from time import sleep
from datetime import datetime,date, timedelta

firebase = firebase.FirebaseApplication('https://cookietest-a4f79.firebaseio.com', None)

now = datetime.now()

# you can pick and choose what to send from below: yearNow is year, monthNow is month etc.

yearNow = now.strftime("%Y")
print("year:", yearNow)

monthNow = now.strftime("%m")
print("month:", monthNow)

dayOfDaMonth = now.strftime("%d")
print("day:", dayOfDaMonth)

timeNow = now.strftime("%H:%M:%S")
print("time:", timeNow)




for x in range(8): # repeat the code below 8 times representing 8 hours

    simulated_people = random.randint(0,30)  # makes up a random number of people
    
    timeSnapshot = datetime.now()
    
    # Where it says (dayOfDaMonth + " " + timeNow), you can replace this with any of the times from line 12 to line 22 above
    data = firebase.patch('/someRandoSimPeopleTimes/' , {dayOfDaMonth + " " + timeNow: simulated_people})
    print(data)
    
    sleep(1)
    print("Sent random timestamps & data to firebase", x+1 , " of 8")
    sleep(1)

