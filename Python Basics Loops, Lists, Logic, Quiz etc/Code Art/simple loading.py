# this program gives you the percentage complete in a loop like a loading bar

# WARNING: On THONNY, it won't overwrite the previous line like it's supposed to. That's a Thonny bug.
# If you run using CTR+T to run in the terminal, it works fine. 

from time import sleep


total_iterations = 30 # this is the bit you change to say how many cycles you want


for i in range(total_iterations):
    
    
    # Your code that is iterating goes here in place of the sleep
    sleep(0.1)
    
    
    percent_complete = round((i/total_iterations)*100,1) # calculates current completion % 
    
    print("Program is", percent_complete,"% Complete ", end = "\r") # prints it over the last line

print("program is complete!")


""" Example output:

 Program is 6.7 % Complete
 
"""