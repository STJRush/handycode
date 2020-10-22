import re
from time import sleep
("=================================================")
print("")
print("")
print("        ,     \    /      ,        ")
print("       / \    )\__/(     / \       ")
print("      /   \  (_\  /_)   /   \      ")
print(" ____/_____\__\@  @/___/_____\____ ")
print("|             |\../|              |")
print("|              \VV/               |")
print("|                                 |")
print("|           TEXT 2 D&D            |")
print("|_________________________________|")
print(" |    /\ /      \\       \ /\    | ")
print(" |  /   V        ))       V   \  | ")
print(" |/     `       //        '     \| ")
print(" `              V                '")
print("")

sleep(0.4)

print("This program translates a text file (to the left) into medieval language. \n")

print("Opening the text document..")

bookFile = open("femaSourceText.txt","r") # Open the file
string=bookFile.read()  #reads the whole book into a big big giant string for python.
string=string.lower() #make it all lowercase. GeTs riD of THis. i!=I , l!=L, p !=P etc.
bookFile.close() #python has the string in it's head now, so can close the text file.

#clean up the file and put each sentence on a new line

#clean_string= re.sub("\n", " ", string)    #join it all back up into one long long line.



clean_string= re.sub("fema", "Shy Crisis Managment Agency ", string)
#clean_string= re.sub("[.]", " \n ", clean_string)
clean_string= re.sub("november", "Month of Uktar", clean_string)

clean_string= re.sub("911", "City Watch Call", clean_string)
clean_string= re.sub("dial", "Summon", clean_string)

clean_string= re.sub("staff", "local peasants", clean_string)
clean_string= re.sub("security", "City Watch", clean_string)
clean_string= re.sub("police", "Town Guards", clean_string)
clean_string= re.sub("telephone", "Spell of Sending or carrier pigeon", clean_string)
clean_string= re.sub("law enforcement", "City Watch", clean_string)
clean_string= re.sub("supervisors", "nobel lords", clean_string)
clean_string= re.sub("employees", "underlings", clean_string)
clean_string= re.sub("workplace", "guild building", clean_string)
clean_string= re.sub("individuals", "royal subjects", clean_string)
clean_string= re.sub("facility", "castle or hovel", clean_string)
clean_string= re.sub("telecommunications", "magical", clean_string)
clean_string= re.sub("routes", "trails", clean_string)
clean_string= re.sub("personnel", "peasants", clean_string)
clean_string= re.sub("management", "nobility", clean_string)
clean_string= re.sub("loudspeaker", "town crier", clean_string)
clean_string= re.sub("e-mail", "high level sending spells", clean_string)
clean_string= re.sub("responders", "City Watchmen", clean_string)
clean_string= re.sub("cmt", "Citywatch Peasant Control Unit", clean_string)
clean_string= re.sub("employee", "village people", clean_string)
clean_string= re.sub("union", "guild", clean_string)
clean_string= re.sub("phone", "royal letter", clean_string)
clean_string= re.sub("national", "King's own", clean_string)
clean_string= re.sub("administrator", "Royal Sherrif", clean_string)
clean_string= re.sub(" u.s.", "New Mondian", clean_string)




clean_string= re.sub("superintendent", "Knight of the Order Commander", clean_string)
clean_string= re.sub("fire", "dragon flame", clean_string)
clean_string= re.sub("union", "guild", clean_string)
clean_string= re.sub("union", "guild", clean_string)
clean_string= re.sub("union", "guild", clean_string)
clean_string= re.sub("union", "guild", clean_string)


clean_string= re.sub("director", "Shadow Council Leader or Cleric", clean_string)
clean_string= re.sub("\.\.\.\.\.", "", clean_string)


print("Changed some words...")

# The next part writes the cleaned up file to a text file that I can open to check it
# all looks nice and neat and ready for finding duplicate lines.

newFile = open("edited_DND_Version.txt", "w") #creates new text file called edited_DND_Version
newFile.write(clean_string) #writes the big long edited string to a this txt file
newFile.close() #closes the file
print("Saved as new file...edited_DND_Version.txt")
print("Here we go...\n \n")
sleep(0.9)
newFile = open("edited_DND_Version.txt", "r") #opens the file again. 
allBookLinesInAList=newFile.readlines() #reads it all into a big big string in it's head

#figures out how many lines there so the program knows when to stop.


#The bit below makes takes a line (n) and compares it to all lines after it (z)
#It might help to imaging "n" as your left finger keeping track of the row and "z" as your right finger going across the columns

print(clean_string)
print("=================================================")
