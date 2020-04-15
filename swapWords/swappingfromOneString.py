import re

# This is the first line from Harry Potter that we will be messing with
originalString = ("Mr. and Mrs. Dursley of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much")

print("-------------------------------------------------")
print("The original string is..")
print("-------------------------------------------------")
print(originalString)



#              replace   THIS with   THIS   in this string
changedString = re.sub("Dursley", "Horseface", originalString) # watch out the last variable is the original string


# we can now just keep writing over the changedString variable
changedString = re.sub("[%&!]", "", changedString)
changedString = re.sub("...", "", changedString)
changedString = re.sub("normal", "on fire", changedString)
changedString = re.sub("number four", "Bally-Go-Backwards", changedString)
changedString = re.sub("Privet", "Smelly", changedString)


print("=================================================")
print("After changing some words with the re module...")
print("=================================================")
print(changedString)


