#playing around with firebase

#sets up the connection to the database

from firebase import firebase
firebase = firebase.FirebaseApplication('https://cookietest-a4f79.firebaseio.com', None)

temperature = 42  #these could come in from a sensor but they're fixed just as an example
humidity = 41


#READING DATA

#reads the database at the node /dht
result = firebase.get('/dht', None)
print(result)

#you can also read along the tree further down /dht/humidity 
result = firebase.get('/dht/humidity', None)
print(result)


#CHANGING/ADDING/REMOVING DATA

#deletes code from the database
firebase.delete('/dht', None)


#Patches on extra data from our temp and humidity variables at the top of the program, simulated sensor readings
result = firebase.patch('/sensor/dht/', {'First_Vals': temperature, 'Sec_Vals': humidity})

#Patches on extra data, you can also hard code in numbers like below
result = firebase.patch('/sensor/dht2/', {'First_Vals': 4, 'Sec_Vals': 2})

#Best to use PATCH instead of PUT or POST as it avoids generating a large random number for the node name


#write to the database (PUT means update current values)
firebase.put("/dht", "/humidity", "0.00")
firebase.put("/dht", "/humidity", "1.00")


#POSTS  to the database (POST means create an entry, does generate a nasty long node name)
data = {"temp": temperature, "humidity": humidity}
firebase.post('/dht', data)


