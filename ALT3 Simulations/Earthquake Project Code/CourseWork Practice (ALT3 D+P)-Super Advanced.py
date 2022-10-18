#this is plenty for LC students to know how to do for their project


import statistics

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

################################ 2010 Data
file = open("2010data.csv","r")
dataIn = file.read()
print (dataIn) # to check values read in
myList5 = dataIn.split("\n")
print ("This is without removing the last list item", myList5) # to check when the items are converted into a list
myList5 = myList5[0:-1] # print my list without the last space
print ("After removing final space", myList5)
myList5 = [float(item) for item in myList5]
print ("float", myList5)
print ("\n")
#Complete the process on data
print ("###### This is the data for 2010 ######")

average5 = statistics.mean(myList5)
print("Average of Magnitudes measured in 2010", average5)
minimum = min(myList5)
print("Minimum measured", minimum)
maximum = max(myList5)
print("Maximum measured", maximum)
print ("\n")


################################ 2011 Data
file = open("2011data.csv","r")
dataIn = file.read()
#print (dataIn) # to check values read in
myList6 = dataIn.split("\n")
#print ("This is without removing the last list item", myList6) # to check when the items are converted into a list
myList6 = myList6[1:-1] # print my list without the last space
#print ("After removing final space", myList6)
myList6 = [float(item) for item in myList6]

#Complete the process on data
print ("###### This is the data for 2011 ######")

average6 = statistics.mean(myList6)
print("Average of Magnitudes measured in 2011", average6)
minimum = min(myList6)
print("Minimum measured", minimum)
maximum = max(myList6)
print("Maximum measured", maximum)
print ("\n")

################################ 2012 Data
file = open("2012data.csv","r")
dataIn = file.read()
#print (dataIn) # to check values read in
myList = dataIn.split("\n")
#print ("This is without removing the last list item", myList) # to check when the items are converted into a list
myList = myList[1:-1] # print my list without the last space
#print ("After removing final space", myList)
myList = [float(item) for item in myList]

#Complete the process on data
print ("###### This is the data for 2012 ######")

average = statistics.mean(myList)
print("Average of Magnitudes measured in 2012", average)
minimum = min(myList)
print("Minimum measured", minimum)
maximum = max(myList)
print("Maximum measured", maximum)
print ("\n")
################################ 2013 Data
file = open("2013data.csv","r")
dataIn = file.read()
#print (dataIn) # to check values read in
myList1 = dataIn.split("\n")
#print ("This is without removing the last list item", myList1) # to check when the items are converted into a list
myList1 = myList1[1:-1] # print my list without the last space
#print ("After removing final space", myList1)
myList1 = [float(item) for item in myList1]

#Complete the process on data
print ("###### This is the data for 2013 ######")

average1 = statistics.mean(myList1)
print("Average of Magnitudes measured in 2013", average1)
minimum = min(myList1)
print("Minimum measurment", minimum)
maximum = max(myList1)
print("Maximum measurment", maximum)
print ("\n")

############################### 2014 Data
file = open("2014data.csv","r")
dataIn = file.read()
#print (dataIn) # to check values read in
myList2 = dataIn.split("\n")
#print ("This is without removing the last list item", myList2) # to check when the items are converted into a list
myList2 = myList2[1:-1] # print my list without the last space
#print ("After removing final space", myList2)
myList2 = [float(item) for item in myList2]

#Complete the process on data
print ("###### This is the data for 2014 ######")

average2 = statistics.mean(myList2)
print("Average of Magnitudes measured in 2014", average2)
minimum = min(myList2)
print("Minimum measurement", minimum)
maximum = max(myList2)
print("Maximum measurement", maximum)
print ("\n")

############################### 2015 Data
file = open("2015data.csv","r")
dataIn = file.read()
#print (dataIn) # to check values read in
myList3 = dataIn.split("\n")
#print ("This is without removing the last list item", myList3) # to check when the items are converted into a list
myList3 = myList3[1:-1] # print my list without the last space
#print ("After removing final space", myList3)
myList3 = [float(item) for item in myList3]

#Complete the process on data
print ("###### This is the data for 2015 ######")

average3 = statistics.mean(myList3)
print("Average of Magnitudes measured in 2015", average3)
minimum = min(myList3)
print("Minimum measurement", minimum)
maximum = max(myList3)
print("Maximum measurement", maximum)
print ("\n")



############################### 2016 Data
file = open("2016data.csv","r")
dataIn = file.read()
#print (dataIn) # to check values read in
myList4 = dataIn.split("\n")
#print ("This is without removing the last list item", myList4) # to check when the items are converted into a list
myList4 = myList4[1:-1] # print my list without the last space
#print ("After removing final space", myList4)
myList4 = [float(item) for item in myList4]

#Complete the process on data
print ("###### This is the data for 2016 ######")

average4 = statistics.mean(myList4)
print("Average of Magnitudes measured in 2016", average4)
minimum = min(myList4)
print("Minimum measurement", minimum)
maximum = max(myList4)
print("Maximum measurement", maximum)
print ("\n")


#######Ploting the graphs###########

year = [2010,2011,2012,2013,2014,2015,2016]
value = [average5,average6,average,average1,average2,average3,average4]
plt.plot(year,value, "gs-")

poly_size = int(input("What polynomial do you want to model:  "))
#draws the trendline for the graph
#np.polyfit(x values, y values, 1 2 or 3) 1-linear, 2 quadratic, 3 cubic
z = np.polyfit(year, value, poly_size)
f = np.poly1d(z)
richter_predict=0
year_predict = int(input("What year would you like to predict: "))

for i in range(poly_size+1):
    richter_predict= richter_predict + z[i]*(year_predict**((poly_size)-i))

plt.title ("Earthquakes Richter Scale 2010 - 2016")
plt.xlabel ("Average per year readings")
plt.ylabel("Ricter scale averages")
plt.legend(["Average mean measurement per Year"])
    #plt.show()
print("The predicted Richter value is: ",round(richter_predict,2))

plt.plot(year,f(year),"r--")
plt.show()





