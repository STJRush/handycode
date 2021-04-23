#playing around with firebase
#sets up the connection to the database

from firebase import firebase
firebase = firebase.FirebaseApplication('https://cookietest-a4f79.firebaseio.com', None)
import csv



#READING all data (keys and values (the full dictionary)) on the node called /moOOARsimData
print("\n Reading this node \n")

#reads the database at the node 
fireBDatas = firebase.get('/moOOARsimData/', None)

print(fireBDatas)

