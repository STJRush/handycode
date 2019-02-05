import os
import time
import csv



def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

print(measure_temp())

#######

f= open("testn.csv", "w", newline="")

wc=csv.writer(f)

for x in range(5):
  wc.writerow([measure_temp()])
  time.sleep(0.2)

f.close()
