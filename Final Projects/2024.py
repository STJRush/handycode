# 2024 Project DM


# DATA ENTRY PART 1:

# Gather data on wellbeing

physical_wellbeing = int(input("On a scale of 1-10 from wrecked to ready, how to you physically feel?"))
emotional_wellbeing = int(input("On a scale of 1-10 from sad to happy, how to you emotionally feel?"))
environmental_wellbeing = int(input("On a scale of 1-10 from nasty to pristine, how would you rate your enviornment?"))



#------------
# Get the average value for wellbeing

from statistics import mean
average_mood = mean([physical_wellbeing, emotional_wellbeing, environmental_wellbeing])

average_mood = round(average_mood,2)

print("So overall you're felling about a", average_mood)
#-------------

# blank list
lightList = []



import serial
from time import sleep

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM9"

ser.open()


# In fact... keep trying it! Again and again! MOAR!
for x in range(9):
        
        # First take in all the data and assign it to this variable
        microbitdata = str(ser.readline())
        
        # Get second bit onwards, call that light_level
        light_level = microbitdata[2:]
        
        # Remove any spaces
        light_level = light_level.replace(" ","")
        
        # Remove any apostrophies
        light_level = light_level.replace("'","")
        
        # Replace this with nothing (remove it)
        light_level = light_level.replace("\\r\\n","")
        
        light_level = float(light_level)
        
        # Print it to see if any of that rubbish above actually worked
        print(light_level)
        
        
        # VALIDATION
        # only add them to the list if they are a float
         
        if type(light_level) == float:
        
            # add it to the list!
            lightList.append(light_level)
        
        
print("My list of light values is.....", lightList)


# Choose my 3 parameters

maxLight = round(max(lightList),2)
minLight = round(min(lightList),2)
meanLight = round(mean(lightList),2)

print("Max light is ",maxLight, "Min light is ",minLight,  "Mean Light is" ,meanLight, )




# Write results to a csv

import csv

path = "Survey_Results.csv"  #your file name, will create or overwrite.
f = open(path, "a", newline='')

csver = csv.writer(f)

csver.writerow([maxLight, minLight, meanLight, average_mood])

print("I have added the following data to your survery_results.csv")
print([maxLight, minLight, meanLight, average_mood])
print("")
f.close()



# Preview what is now in the spreadsheet using pandas

import pandas as pd

df = pd.read_csv('Survey_Results.csv')

print(df)


