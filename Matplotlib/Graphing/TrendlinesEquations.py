#calc the trendline
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv = pd.read_csv('Pirates.csv')

#select your data columns
data = csv[['Pirates', 'Temp']]

#Lets you say which will be x and y
x = data['Pirates']
y = data['Temp']

#choose your graph type
plt.scatter(x, y)

#some maths
z = np.polyfit(x, y, 1) #1 is linear, 2 is quadratic, 3 is cubic (polynomial fun!)
f = np.poly1d(z) #1d is a line. There's no 2d because you can't have a 2d line, that's a square.
plt.plot(x,f(x),"r--") #plot

#z returns two values in a list eg. [-3.91792431e-05  1.56428161e+01]
#The first value z[0] is the slope and the second x[1] is the y intercept
print("z will give you ", z)


print("The slope is", z[0])
print("The intercept is", z[1])

#here we can round off things to 2 digits so that the equation isn't too ugly and long
#This is the equation of a line    y=        m             x    +    c
print("The equation of the line is y="+str(round(z[0],2))+"x+"+str(round(z[1],2)))

#shows your graph in a new window
plt.show()



#The .csv file used in this example looks like this:

# Pirates	Temp	  Year
# 45000	  14.06	  1820
# 35000	  14.25	  1860
# 20000	  14.61	  1880
# 15000	  14.91	  1920
# 5000	  15.41	  1940
# 3000	  15.52	  1980
# 17	  15.92	  2000
