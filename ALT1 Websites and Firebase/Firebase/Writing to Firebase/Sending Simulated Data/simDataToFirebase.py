#sends a bunch of random fake temperatures to firebase

from firebase import firebase
import random
from time import sleep

firebase = firebase.FirebaseApplication('https://cookietest-a4f79.firebaseio.com', None)


for x in range(10): # repeat the code below 10 times

    simulated_temperature = random.randint(18,21)  # makes up a random temperature between 18 and 21
    simulated_humidity = random.randint(55,59) # makes up a random hunmidity between 55 and 59

    # attatches names to the data
    data = {"SimTemp": simulated_temperature, "SimHumid": simulated_humidity}
    
    #POSTS  to the database (POST means create an entry, does generate a nasty long node name)
    firebase.post('/simData', data)
    sleep(1)
    print("Sent random temp to firebase", x+1 , " of 10")
    sleep(1)
    
    
 """
 One issue with this code is that it generates unique identifiers for each datapoint.
 That's kind of annoying. There's a tidy version of this code in this same folder in the repository 
    
-MPjzXK7pqANMr586Z2w
-MW94W9aNYK6-QxyF-Wy
-MW94Wt3uOIP_GTrnzn9
SimHumid: 
58
SimTemp: 
21
-MW94X_ov2K0f3O-nGUJ
-MW94YH_4D-AelrQ0rkH
-MW94YzJk3tqNw87vL32
    
    
"""
