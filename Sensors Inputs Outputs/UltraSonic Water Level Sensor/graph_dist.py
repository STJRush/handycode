#run in python 3

from gpiozero import CPUTemperature #gpiozero module must be downloaded for py3
import RPi.GPIO as GPIO

from time import sleep, strftime, time
import matplotlib.pyplot as plt     #matplotlib module must be downloaded for py3

GPIO.setmode(GPIO.BCM)
print ("Distance Measurement In Progress")

TRIG = 23      #from now on, port 23 we will call TRIG
ECHO = 24      #from now on, port 24 we will call ECHO

GPIO.setup(TRIG,GPIO.OUT)  #sets up pin 23 to trigger a ping sound out!
GPIO.setup(ECHO,GPIO.IN)   #sets up pin 24 to listen for a pong echo in!

GPIO.output(TRIG, False)   #stops any echo from a previous program that might still be going


firstrun = 1
print ("Waiting For Sensor To Settle")
sleep(3)


plt.ion()

x = []  #placeholders for the graph later on
y = []


def distcheck():
  count = 0
  global firstrun
  
  maxTolerance = 1.3   #does not allow any measurement 30% above average
  minTolerance = 0.7   #does not allow any measurement less than 70% below average

  while True:
    sleep(0.1)
    GPIO.output(TRIG, True)  #fires a pulse
    sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:  #measure some times
      pulse_start = time()

    while GPIO.input(ECHO)==1:
      pulse_end = time()

    pulse_duration = pulse_end - pulse_start  #does the maths


    # The next values are "global", meaning the distance values from here can be used outside of this function.
    # "global" changes the value of distance everywhere. Without making these global, the graph later
    # on would keep reading 0 even though distance in this function would be updating. The change to distance
    # would never leave the bounds of this function.

    distance = pulse_duration * 17150   #distance = time * speed of sound

    global distance; distance = round(distance, 2)       #rounds distance values off to 2 places

    print ("Distance:",distance,"cm")                    #adds units to make it look neater



      #This below is very messy but it helps stop a jumpy graph full of freak echos and errors.
      #The graph looks a lot better now. The code does not. Here's how it works:
      #The sensor measures distance 10 times
      #These 10 measurements are averaged into one average value
      #For each of the next 10 measurments, each value is checked against the
      #previous average value. There shouldn't be much change in water level.
      #The water level will not increase 50cm in half a second. If it measures this, it's an false echo.
      #If there's a big difference between the measured distance and the average, the measurement is deleted and all
      #ten measurements are taken again.
      #The error checking algorithms need to become functions as this code is waaaaaaay too long!



    if count == 0:
      distVal1 = distance

      print("Distance value 1:")




      #Error checking algorithm
      if firstrun == False: #if not the first set of 10 points

        
        check = distVal1/average #compare this value to the last average of 10 points

        if check < minTolerance or check > maxTolerance:  #if it's a change greater than +/- 5% (a likely error)

          print("Anomoly!, skip this value")
          sleep(1)
          count = 0      #start these 10 measurments all over again as there was a wee anomaly
          
        else:

          count = count + 1  #if it's within 5% move on to the next measurement
          print("CHECKS OUT!")

      elif firstrun == True:
        print("calibrating...")
        count = count + 1    #if it's the very first set of 10 measurements, just move on as there's no comparison yet.
      else:
        print("EROROROROROROOROORO!!!")


      
    elif count ==1:
      distVal2 = distance

           #Error checking algorithm
      if firstrun == False: #if not the first set of 10 points

        
        check = distVal2/average #compare this value to the last average of 10 points

        if check < minTolerance or check > maxTolerance:  #if it's a change greater than +/- 5% (a likely error)

          print("Anomoly!, skip this value")
          sleep(1)
          count = 0      #start these 10 measurments all over again as there was a wee anomaly
          
        else:

          count = count + 1  #if it's within 5% move on to the next measurement
          print("CHECKS OUT!")

      elif firstrun == True:
        print("calibrating...")
        count = count + 1    #if it's the very first set of 10 measurements, just move on as there's no comparison yet.
      else:
        print("EROROROROROROOROORO!!!")

      print("Distance value 2:")
      

      
    elif count ==2:
      distVal3 = distance
     #Error checking algorithm
      if firstrun == False: #if not the first set of 10 points

        
        check = distVal3/average #compare this value to the last average of 10 points

        if check < minTolerance or check > maxTolerance:  #if it's a change greater than +/- 5% (a likely error)

          print("Anomoly!, skip this value")
          sleep(1)
          count = 0      #start these 10 measurments all over again as there was a wee anomaly
          
        else:

          count = count + 1  #if it's within 5% move on to the next measurement
          print("CHECKS OUT!")

      elif firstrun == True:
        print("calibrating...")
        count = count + 1    #if it's the very first set of 10 measurements, just move on as there's no comparison yet.
      else:
        print("EROROROROROROOROORO!!!")
      print("Distance value 3:")



      
    elif count ==3:
      distVal4 = distance

     #Error checking algorithm
      if firstrun == False: #if not the first set of 10 points

        
        check = distVal4/average #compare this value to the last average of 10 points

        if check < minTolerance or check > maxTolerance:  #if it's a change greater than +/- 5% (a likely error)

          print("Anomoly!, skip this value")
          sleep(1)
          count = 0      #start these 10 measurments all over again as there was a wee anomaly
          
        else:

          count = count + 1  #if it's within 5% move on to the next measurement
          print("CHECKS OUT!")

      elif firstrun == True:
        print("calibrating...")
        count = count + 1    #if it's the very first set of 10 measurements, just move on as there's no comparison yet.
      else:
        print("EROROROROROROOROORO!!!")
      print("Distance value 4:")

      
    elif count ==4:
      distVal4 = distance
      #Error checking algorithm
      if firstrun == False: #if not the first set of 10 points

        
        check = distVal4/average #compare this value to the last average of 10 points

        if check < minTolerance or check > maxTolerance:  #if it's a change greater than +/- 5% (a likely error)

          print("Anomoly!, skip this value")
          sleep(1)
          count = 0      #start these 10 measurments all over again as there was a wee anomaly
          
        else:

          count = count + 1  #if it's within 5% move on to the next measurement
          print("CHECKS OUT!")

      elif firstrun == True:
        print("calibrating...")
        count = count + 1    #if it's the very first set of 10 measurements, just move on as there's no comparison yet.
      else:
        print("EROROROROROROOROORO!!!")     
      count = 5
      print("Distance value 5:")
    elif count ==5:
      distVal5 = distance
     #Error checking algorithm
      if firstrun == False: #if not the first set of 10 points

        
        check = distVal5/average #compare this value to the last average of 10 points

        if check < minTolerance or check > maxTolerance:  #if it's a change greater than +/- 5% (a likely error)

          print("Anomoly!, skip this value")
          sleep(1)
          count = 0      #start these 10 measurments all over again as there was a wee anomaly
          
        else:

          count = count + 1  #if it's within 5% move on to the next measurement
          print("CHECKS OUT!")

      elif firstrun == True:
        print("calibrating...")
        count = count + 1    #if it's the very first set of 10 measurements, just move on as there's no comparison yet.
      else:
        print("EROROROROROROOROORO!!!")
      print("Distance value 6:")
    elif count ==6:
      distVal6 = distance
     #Error checking algorithm
      if firstrun == False: #if not the first set of 10 points

        
        check = distVal6/average #compare this value to the last average of 10 points

        if check < minTolerance or check > maxTolerance:  #if it's a change greater than +/- 5% (a likely error)

          print("Anomoly!, skip this value")
          sleep(1)
          count = 0      #start these 10 measurments all over again as there was a wee anomaly
          
        else:

          count = count + 1  #if it's within 5% move on to the next measurement
          print("CHECKS OUT!")

      elif firstrun == True:
        print("calibrating...")
        count = count + 1    #if it's the very first set of 10 measurements, just move on as there's no comparison yet.
      else:
        print("EROROROROROROOROORO!!!")
      print("Distance value 7:")
    elif count ==7:
      distVal7 = distance
     #Error checking algorithm
      if firstrun == False: #if not the first set of 10 points

        
        check = distVal7/average #compare this value to the last average of 10 points

        if check < minTolerance or check > maxTolerance:  #if it's a change greater than +/- 5% (a likely error)

          print("Anomoly!, skip this value")
          sleep(1)
          count = 0      #start these 10 measurments all over again as there was a wee anomaly
          
        else:

          count = count + 1  #if it's within 5% move on to the next measurement
          print("CHECKS OUT!")

      elif firstrun == True:
        print("calibrating...")
        count = count + 1    #if it's the very first set of 10 measurements, just move on as there's no comparison yet.
      else:
        print("EROROROROROROOROORO!!!")
      print("Distance value 8:")
    elif count ==8:
      distVal8 = distance
     #Error checking algorithm
      if firstrun == False: #if not the first set of 10 points

        
        check = distVal8/average #compare this value to the last average of 10 points

        if check < minTolerance or check > maxTolerance:  #if it's a change greater than +/- 5% (a likely error)

          print("Anomoly!, skip this value")
          sleep(1)
          count = 0      #start these 10 measurments all over again as there was a wee anomaly
          
        else:

          count = count + 1  #if it's within 5% move on to the next measurement
          print("CHECKS OUT!")

      elif firstrun == True:
        print("calibrating...")
        count = count + 1    #if it's the very first set of 10 measurements, just move on as there's no comparison yet.
      else:
        print("EROROROROROROOROORO!!!")    
      print("Distance value 9:")
    elif count ==9:
      distVal8 = distance
     #Error checking algorithm
      if firstrun == False: #if not the first set of 10 points

        
        check = distVal8/average #compare this value to the last average of 10 points

        if check < minTolerance or check > maxTolerance:  #if it's a change greater than +/- 5% (a likely error)

          print("Anomoly!, skip this value")
          sleep(1)
          count = 0      #start these 10 measurments all over again as there was a wee anomaly
          
        else:

          count = count + 1  #if it's within 5% move on to the next measurement
          print("CHECKS OUT!")

      elif firstrun == True:
        print("calibrating...")
        count = count + 1    #if it's the very first set of 10 measurements, just move on as there's no comparison yet.
      else:
        print("EROROROROROROOROORO!!!") 
      print("Distance value 10:")
    elif count ==10:
      distVal9 = distance
     #Error checking algorithm
      if firstrun == False: #if not the first set of 10 points

        
        check = distVal9/average #compare this value to the last average of 10 points

        if check < minTolerance or check > maxTolerance:  #if it's a change greater than +/- 5% (a likely error)

          print("Anomoly!, skip this value")
          sleep(1)
          count = 0      #start these 10 measurments all over again as there was a wee anomaly
          
        else:

          count = count + 1  #if it's within 5% move on to the next measurement
          print("CHECKS OUT!")

      elif firstrun == True:
        print("calibrating...")
        count = count + 1    #if it's the very first set of 10 measurements, just move on as there's no comparison yet.
      else:
        print("EROROROROROROOROORO!!!")
    elif count ==11:
      distVal10 = distance
      #Error checking algorithm
      if firstrun == False: #if not the first set of 10 points

        
        check = distVal10/average #compare this value to the last average of 10 points

        if check < minTolerance or check > maxTolerance:  #if it's a change greater than +/- 5% (a likely error)

          print("Anomoly!, skip this value")
          sleep(1)
          count = 0      #start these 10 measurments all over again as there was a wee anomaly
          
        else:

          count = count + 1  #if it's within 5% move on to the next measurement
          print("CHECKS OUT!")

      elif firstrun == True:
        print("calibrating...")
        count = count + 1    #if it's the very first set of 10 measurements, just move on as there's no comparison yet.
      else:
        print("EROROROROROROOROORO!!!")     
      

      total= distVal1 + distVal2 + distVal3 + distVal4 + distVal5 + distVal6 + distVal7 + distVal8 + distVal9 + distVal10
      global average; average = total/10
      print("Average value: " + str(average))
      break
    
    else:
      print("errors oh no")
      


######################
#program starts here
  #######################


firstrun = True

while True:

    distcheck()  #checks distance
    
    firstrun=False


    #writes this data to a table (a .csv file)
    with open("cpu_dist.csv", "a") as log:   # "a" means append to the end
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(average)))
        

    y.append(average)  #puts the distance values on the y-axis
    x.append(time())    #puts the distance values on the x-axis
    plt.clf()
    plt.scatter(x,y)    #chooses the scatter plot chart type
    plt.plot(x,y)
    plt.draw()          #draws the graph (or if an a loop, updates the graph)

    sleep(0.01)         #Waits between measurements. This could be made longer to save power.
