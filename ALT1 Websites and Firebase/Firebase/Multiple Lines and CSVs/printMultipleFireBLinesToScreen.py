#playing around with firebase
#sets up the connection to the database

from firebase import firebase
firebase = firebase.FirebaseApplication('https://cookietest-a4f79.firebaseio.com', None)


fireBDatas = firebase.get('/moOOARsimData/', None)



#Printing ALLLLLLLLL THE DATA from a firebase node
print("\n Printing out all values \n ")

# this is a dictionary (a python database datatype so we need to pull out values into a list)
for x in fireBDatas: # go through the dictionary of keys and values eg. Temp(key):53(value)
    
  print(x) # print out the key
  print(fireBDatas[x]) # print out just the value

