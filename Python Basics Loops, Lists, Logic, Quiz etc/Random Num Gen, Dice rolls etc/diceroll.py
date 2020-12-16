import random
import statistics

def d(n): # rolls a dice eg d(8) or d(20)
  roll = random.randint(1,n) # makes a random integer between 0 and n
  return roll # takes the roll back out of the fuction to use in your game)

listyMacListFace = []

for x in range(9001):
    listyMacListFace.append(d(20))
    
print(listyMacListFace)

eeenymeany = statistics.mean(listyMacListFace)
print("mean:", eeenymeany)