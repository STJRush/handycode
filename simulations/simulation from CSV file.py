##THE PLAN

## need to get a single x element (single word) from the big list using dataListed[0][0]
## clean it using a function clean_stuff(valu)
## add it to the x list
## make a for loop to do this for all x values in range row_count

## need to get a single y element (single word) from the big list using dataListed[0][1]
## clean it using a function clean_stuff(valu)
## add it to the y list
## make a for loop to do this for all x values in range row_count

## End up two clean lists, one with x values and one with y values

## We can now graph them or whatever. Or print the back to a nice clean .csv
import pandas as pd
import numpy as np
import csv
import re
import matplotlib.pyplot as plt

#"valu" should be a string going into the function to get cleaned
def clean_stuff(valu):
    
    valu = re.sub('[.!@%#$]', '', valu) #re sub out symbols
    valu = re.sub('Mr', '', valu) #re sub out Mr
    valu = re.sub(' points', '', valu) #re sub out single space
    valu = re.sub(' ', '', valu) #re sub out single space
    return valu #send it back all sqeaky clean


f = open("dirtyData.csv", newline = '') #this is the file we will get dirty data from
reader = csv.reader(f)

#header = next(reader)

dataListed= [row for row in reader] #turns the data into a bit list


#Counts how many rows in the csv file. We'll need this later to limit loops.
row_count = sum(1 for row in dataListed) 
print("number of rows is", row_count)


print("Here is the original list of dirty data..")
print(dataListed, "\n\n")

print("Here is the cleaned up list that will be written to the new csv and/or graphed")

xValuesList=[]
## need to get a single x element (single word) from the big list using dataListed[0][0]
## clean it using a function clean_stuff(valu)
## add it to the x list
## make a for loop to do this for all x values in range row_count

for i in range(row_count):       #stop at the end of the last row
    valu = dataListed[i][0]        #[0][0] is the first point. [1][0] is next down etc.
    cleanxVal=clean_stuff(valu)    #send it to the cleaners
    xValuesList.append(cleanxVal)  #take it back and add it to our final xValuesList

print(xValuesList)



yValuesList=[]
## need to get a single y element (single word) from the big list using dataListed[0][1]
## clean it using a function clean_stuff(valu)
## add it to the y list
## make a for loop to do this for all x values in range row_count

for i in range(row_count):       #stop at the end of the last row
    valu = dataListed[i][1]        #[0][1] is the first y point. [1][1] is next down etc
    cleanyVal=clean_stuff(valu)    #send it to the cleaners
    yValuesList.append(cleanyVal)   #take it back and add it to our final yValuesList

print(yValuesList)

f.close()


################################# write the values to a new .csv file

path = "cleanedData.csv"  #your file name, will create or overwrite.
f = open(path, "w", newline='')

csver = csv.writer(f)

#write all of the x,y values into a csv. Limit it to the number of rows.
for i in range(row_count):
    csver.writerow([xValuesList[i], yValuesList[i]])
    
f.close()


#calc the trendline and plots the graph
csv = pd.read_csv('cleanedData.csv')
data = csv[['Dist', 'Time']]
x = data['Dist']
y = data['Time']



plt.scatter(x, y)

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")
plt.xlabel('Time')
plt.ylabel('Distance')

print("The slope is", z[0])
print("The intercept is", z[1])
print("The equation of the line is y="+str(round(z[0],2))+"x+"+str(round(z[1],2)))

plt.savefig('graph.png')
plt.show()



############## Now take the equation and use it as a model

print("Welcome to the simulator")

xAxisTitle = xValuesList[0]
yAxisTitle = yValuesList[0]

print("Your data has show that the relationship between ", xValuesList[0], "and ", yValuesList[0], "is the following:")
print(yAxisTitle, "=", str(round(z[0],2)), " x ", xAxisTitle, str(round(z[1],2)))

print("We will now create a simulator based on your data")


from tkinter import *

def sel():
   selection = xAxisTitle+"= " + str(timevar.get())
   distlabel.config(text = selection)
   
   selection = yAxisTitle+"=" + str((timevar.get()*z[0])+z[1])  #
   anslabel.config(text = selection)
   
   
    
root = Tk()

#sets sliders to accept floats as their values
timevar = DoubleVar()

#title label
toplabel = Label(root)
toplabel.config(text = "Choose time to simulate")
toplabel.pack()


#time scale
scale = Scale( root, variable = timevar )
scale.pack(anchor = CENTER)


button = Button(root, text = "Select Value", command = sel)
button.pack(anchor = CENTER)

distlabel = Label(root)
distlabel.pack()

anslabel = Label(root)
anslabel.pack()


background_image=PhotoImage(file="graph.png")
background_label = Label(root, image = background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.pack()
#root.wm_geometry("600x400+20+40")

##

root.mainloop()