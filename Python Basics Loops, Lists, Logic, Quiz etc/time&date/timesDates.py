from time import sleep
from datetime import datetime



now = datetime.now()

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

