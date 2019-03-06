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


import csv
import re

#"valu" should be a string going into the function to get cleaned
def clean_stuff(valu):
    
    valu = re.sub('[.!@#$]', '', valu) #re sub out symbols
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
