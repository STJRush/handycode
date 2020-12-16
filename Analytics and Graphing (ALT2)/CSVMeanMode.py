############### FINDING THE MEAN OF A COLUMN IN A CSV FILE

import statistics
import csv

# opens the csv
f = open("cleaned.csv", newline='')
reader = csv.reader(f)


# makes a list from the first column. The int() makes each string(word) from the text file into an integer(number)
dataListedSeriesA = [int(column[1]) for column in reader]
print(dataListedSeriesA)

xValuesMean = statistics.mean(dataListedSeriesA)
print("The mean is ", xValuesMean)


xValuesMedian = statistics.median(dataListedSeriesA)
print("The median is ", xValuesMedian)

xValuesVari = statistics.variance(dataListedSeriesA)
print("The variance is ", xValuesVari)


xValuesHar = statistics.harmonic_mean(dataListedSeriesA)
print("The Harmonic Mean is ", xValuesHar)





# The mode can sometimes have an error if there is more than one most common number
try:
    xValuesMode = statistics.mode(dataListedSeriesA)
    print("The Mode is ", xValuesMode)

except:
    print("Plot twist...THERE IS NO MODE!")








"""
The csv used for this example:

2013,4,5   
2013,4,5
2014,6,7
2015,8,8
2016,15,9
2017,15,10
"""
