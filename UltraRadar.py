#!/usr/bin/python
#
# ultrasonic_sensor.py
# Measure distance using an ultrasonic module
# in a loop.
#

# -----------------------
# Import required Python libraries
# -----------------------
import time
import RPi.GPIO as GPIO
import datetime

import plotly.plotly as py
from plotly.graph_objs import Data, Scatter, Stream

#plotly_api_settings
print("plotly cred checking")
stream_id = 'your_streaming_id'
username ='your_username'
api_key ='your_api_key'

py.sign_in(username, api_key)



# -----------------------
# Define some functions
# -----------------------

def measure():
  print("inside measure")
  # This function measures a distance

  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()
  
  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()

  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()

  elapsed = stop-start
  distance = (elapsed * 34300)/2

  return distance

def plot_graph():
  py.plot(Data([Scatter(x=[],y=[],
                      stream=Stream(token=stream_id,maxpoints=100))]))
   
  #heartbeat(self,reconnect_on=(200, '',408))
  #open(self)
  #write(self,trace,layout=None,Validate=True,reconnect_on=(200, '',408))
  
# -----------------------
# Main Script
# -----------------------

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO    = 24

print "Ultrasonic Measurement"

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:

  stream = py.Stream(stream_id)
  stream.open()
    
  plot_graph()

  while True:

    distance = measure()
    print "Distance : %.1f" % distance
    time.sleep(1)
    
    
    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    y = distance

    stream.write(dict(x=x, y=y))
    time.sleep(1)
  stream.close()

    
    #open("file.txt","w").write(datetime.time.now().ctime())
    
    

except KeyboardInterrupt:
  # User pressed CTRL-C
  # Reset GPIO settings
  GPIO.cleanup()
