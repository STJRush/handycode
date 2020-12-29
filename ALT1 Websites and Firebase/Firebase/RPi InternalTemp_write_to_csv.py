import os
import time
import csv



def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

print(measure_temp())

######## Takes 5 reading from temp sensor and writes them to a .csv #########


f= open("testn.csv", "w", newline="") #give your .csv file a name

wc=csv.writer(f)

for x in range(5):                    #take five readings
  wc.writerow([measure_temp()])       #writes distance into the next row

f.close()                             #close the file when done to prevent data loss
