#This program will print a random number from 1-10


import random           # Let's you use the random fuction in your program. You must include this at the very start of your program.

number=random.random()  # Makes a random mumber and calls it "number". You can call it anything, "number" is just a variable name.
number=10*number        # As the number is from 0.1 to 1.0, we need to multiple it by 10 so it looks nice. Things should look nice.
print(int(number))      # Prints the number and makes sure it's an integer eg. 1,2,3 like on Sesame street. Not like 2.33232452.
