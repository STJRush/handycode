import os

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

current_CPU_Temp = measure_temp()

print(current_CPU_Temp)
