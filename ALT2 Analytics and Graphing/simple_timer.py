# Simple Timer Code

from time import time as time_now
from time import sleep

# Record the Start time
start_time = time_now()

while True:
    elapsed_time = round(time_now() - start_time)
    print("Elapsed time:", elapsed_time)
    sleep(1)  # Pauses the loop for 1 second
