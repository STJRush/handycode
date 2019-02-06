import csv

path = "waa.csv"  #your file name, will create or overwrite.
f = open(path, "w", newline='')

csver = csv.writer(f)

csver.writerow(["row1column1", "row1column2"])
csver.writerow(["row2column1", "row2column2"])

f.close()
