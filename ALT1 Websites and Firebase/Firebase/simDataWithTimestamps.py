from firebase import firebase
import random
from time import sleep
from datetime import datetime

firebase = firebase.FirebaseApplication('https://cookietest-a4f79.firebaseio.com', None)


now = datetime.now() #gets the date & time from your computer right now

print("The full datetime object from the computer is", now)

print("\n We don't want all that, so we can just pick out parts of the object using strftime. \n")


# It's not necessary to list all of these in your own program, think of this a selection box of delicious
# chocolate chunks of code to choose from.



yearNow = now.strftime("%Y")
print("year:", yearNow)

monthNow = now.strftime("%m")
print("month:", monthNow)

dayOfDaMonth = now.strftime("%d")
print("day:", dayOfDaMonth)

timeNow = now.strftime("%H:%M:%S")
print("time:", timeNow)

hoursNow = now.strftime("%H")
print("hours:", hoursNow)

minsNow = now.strftime("%M")
print("mins:", minsNow)

secsNow = now.strftime("%S")
print("seconds:", secsNow)


# Remember to include the now = datetime.now() code inside your loop or it'll only take the time once


print("\n Normally, a datapoint will be like 'Temperature:23' but instead of the name Temperature,")
print("we'll use now.strftime('%H:%M:%S') as the name of the data point which is the time now. \n" )

for count in range(8): # repeat the code below 8 times representing 8 hours

    simulated_people = random.randint(0,30)  # makes up a random number of people
    
    now = datetime.now() #gets the date & time from your computer right now each time
    
    # patches up the firebase the Name (time right now) : The value which is a random number from 1-30
    data = firebase.patch('/someRandoSimPeopleTimes/' , {now.strftime("%H:%M:%S"): simulated_people})
    print(data)
    
    sleep(1)
    # It's count + 1 because computers start counting at 0 and humans start counting from 1
    print("Sent random data & real timestamps to firebase", count+1 , " of 8")
    sleep(1)


