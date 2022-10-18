import matplotlib.pyplot as plt
import numpy as np

file = open ("Hits.csv","r")
hitsIn = file.read()
file.close()
hitsIn = hitsIn.split(",")
hitsIn.remove(hitsIn [-1])
#print (hitsIn)
#hitsIn = float(hitsIn)
#hitsIn = round (hitsIn,2)
hitsIn  = [float(item) for item in hitsIn ]

file = open ("Days.csv","r")
days = file.read()
file.close()
days = days.split(",")
days.remove(days [-1])
days  = [float(item) for item in days ]

x= days
y=hitsIn

plt.scatter(x, y)

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")
plt.xlabel('Time')
plt.ylabel('Distance')

print("The slope is", z[0])
print("The intercept is", z[1])
print("The equation of the line is y="+str(round(z[0],2))+"x+"+str(round(z[1],2)))

UserDay = int(input("Enter Day to you want to know how hits you will have: "))
y=z[0]*(UserDay)+(z[1])

print ("The number of hit you will have on that day ", y)

plt.scatter(days,hitsIn)

plt.title("Hits V Days")
plt.xlabel("Days")
plt.ylabel("Hits")
plt.show()