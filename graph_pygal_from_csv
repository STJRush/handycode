# install pygal and lxml packages before running this code
import pygal
import csv

#Turning pairs of columns into x,y series for graphing
######################################################

#series name = [[int(first column of data), int(second column of data)] for column in reader]
#REMEMBER: column[0] is the first column, column[1] is the second etc.

#opens the csv
f = open("myDatas.csv", newline = '')
reader = csv.reader(f)
#makes a list from the first and second columns
dataListedSeriesA = [[int(column[0]), int(column[1])] for column in reader]
f.close()

#opens the csv
f = open("myDatas.csv", newline = '')
reader = csv.reader(f)
#makes a list from the first and third columns
dataListedSeriesB = [[int(column[0]), int(column[2])] for column in reader]
f.close()

#you have to close the file between reading each series, no idea why.


#Graphing the series using pygal
######################################################

disChart = pygal.XY(stroke=False)

#chart title
disChart.title = 'Correlation'

#disChart.add('Series Name', [lists of data points])
disChart.add('A', dataListedSeriesA)
disChart.add('B', dataListedSeriesB)

#save top a vector graphics file
disChart.render_to_file('chart.svg')

#show in your bcolumnser
disChart.render_in_browser()

"""
The csv used for this example:
    
2013,4,5
2014,6,7
2015,8,8
2016,11,9
2017,15,10
"""
