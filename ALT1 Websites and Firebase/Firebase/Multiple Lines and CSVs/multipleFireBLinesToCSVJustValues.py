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


#READING ALLLLLLLLL THE DATA from a firebase node and writing it to a CSV

print("\n Writing all keys and values to a csv file \n ")

f= open("justValuesFromFirebase.csv", "w", newline="") #give your .csv file a name
wc=csv.writer(f)

for x in fireBDatas:                   # iterate through the whole node (dictionary)
    
    wc.writerows( [[fireBDatas[x]]] )      #writes values for each key to a row in the csv, then makes a new line

f.close()                             #close the file when done to prevent data loss



print("\n Writing complete. Open justValuesFromFirebase.csv to view data. It's in the same folder as this python program. ")


"""
Example Output in justValuesFromFirebase.csv.csv file:

19
18
18
18
21
19
19
19
20
19


"""

