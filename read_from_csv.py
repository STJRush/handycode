import csv

f = open("DistTime.csv", newline = '') #this file needs to exist
reader = csv.reader(f)

header = next(reader)

# This next line magically turns the csv file into a GIANT list.
# If there's two columns, each element has a sublist of two values
# If there's three columns, each element has a sublist of three values etc. etc.
dataListed= [row for row in reader] 

#print(dataListed) #prints the list. Yes it's an ugly mess of list within lists but..


#now we can pick the first row using
print("The first row is ", (dataListed[0]))

""" HOW THIS WORKS:
Distance     Time
   2          23
   4          34
   6          56

print(dataListed[0]) will give you the first row [2, 23]
"""


#and inside, that row, the first element
print("Just one element is", (dataListed[0])[0])


"""HOW THIS WORKS:
Distance     Time
   2          23
   4          34
   6          56

print(dataListed[0][0]) will give you the first row 2

"""



# it's like saying I want the thing in row 1, column 2 except
# that in python we always count from zero, not one.

f.close()





"""
for x in reader: #prints a list of the paired values but seperately, not as one big list
    print(x)
"""


