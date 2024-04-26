
import pandas as pd

df = pd.read_csv('Survey_Results.csv')

print(df)

# Print Table Of Scores
colnames = ['Emotional','Physical','Environmental','Average']

df = pd.read_csv('Survey_Results.csv', skiprows=[0], names=colnames)
#data = pandas.read_csv('BigShtats.csv', skiprows=[0], names=colnames)

# print a list of values in the first column
list_Of_Values_In_First_Column = df.Emotional.tolist()
print("Here is a list of values in the first column:", list_Of_Values_In_First_Column)


# print a list of values in the second column
list_Of_Values_In_Second_Column = df.Physical.tolist()
print("Here is a list of values in the first column:", list_Of_Values_In_Second_Column)
