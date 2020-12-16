import random
import statistics

def d(n): #rolls a dice eg d(8) or d(20)
  roll = random.randint(1,n)
  return roll

listy=[]

for i in range (1000):
    listy.append(d(20))

print(listy)
print("mean:", statistics.mean(listy))

print(d(6))