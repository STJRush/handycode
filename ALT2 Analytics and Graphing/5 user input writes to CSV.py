# Gather data on wellbeing

physical_wellbeing = int(input("On a scale of 1-10 from wrecked to ready, how to you physically feel?"))
emotional_wellbeing = int(input("On a scale of 1-10 from sad to happy, how to you emotionally feel?"))
environmental_wellbeing = int(input("On a scale of 1-10 from nasty to pristine, how would you rate your enviornment?"))


# Get the average value for wellbeing

from statistics import mean
average_mood = mean([physical_wellbeing, emotional_wellbeing, environmental_wellbeing])

average_mood = round(average_mood,2)

print("So overall you're felling about a", average_mood)



# Write results to a csv

import csv

path = "Survey_Results.csv"  #your file name, will create or overwrite.
f = open(path, "a", newline='')

csver = csv.writer(f)

csver.writerow([physical_wellbeing, emotional_wellbeing, environmental_wellbeing, average_mood])

print("I have added the following data to your survery_results.csv")
print([physical_wellbeing, emotional_wellbeing, environmental_wellbeing, average_mood])
print("")
f.close()



# Preview what is now in the spreadsheet using pandas

import pandas as pd

df = pd.read_csv('Survey_Results.csv')

print(df)
