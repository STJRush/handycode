# modified from https://stackoverflow.com/questions/20518122/python-working-out-if-time-now-is-between-two-times

import datetime

def is_hour_between(start, end):
    
    # Get the time now
    now = datetime.datetime.now().time()
    print("The time now is", now)
    
    # Format the datetime string to just be hours and minutes
    time_format = '%H:%M'
    
    # Convert the start and end datetime to just time
    start = datetime.datetime.strptime(start, time_format).time()
    end = datetime.datetime.strptime(end, time_format).time()

    is_between = False
    is_between |= start <= now <= end
    is_between |= end <= start and (start <= now or now <= end)
    
    return is_between

check = is_hour_between('08:30', '15:30') #spans to the next day

print("time check", check) # result = True
