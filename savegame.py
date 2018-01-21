


################################
# HOW TO WRITE TO A SAVED FILE #
################################


# say you have some values..
health = 10
gold = 20

# makes or opens a save file called Saveytime.py
f = open("Saveytime.py", "w")


# writes the values to the file

f.write("health = " + str(health) + "\n")
f.write("gold = " + str(gold) + "\n")

"""
What the above lines mean:

f.write() writes to your file

str(health) takes the value of health (10) and makes it a string so that it can be
joined with a + to the string "health = "

"\n" hits the enter key to make the next line underneath the previous one

"""


# closes the file to prevent it ending up a sad, blank empty file
f.close()

#########################################
# How to read from a saved python file: #
#########################################


# At the START, the START of your program, write...

# from [Whatever Your Saved File is called] import * (the astrix means everything as in, import everything)
# eg. 

from Saveytime import *
