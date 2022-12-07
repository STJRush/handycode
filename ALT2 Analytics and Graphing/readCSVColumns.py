
import pandas
# Print Table Of Scores
colnames = ['PlayerName','Shots','Opponent','Won','Lost','Difference']
data = pandas.read_csv('BigShtats.csv', skiprows=[0], names=colnames)
print(data)

listOfShotsCSV = data.Shots.tolist()
print(listOfShotsCSV)

listOfShotsCSV.sort()
print(listOfShotsCSV)
