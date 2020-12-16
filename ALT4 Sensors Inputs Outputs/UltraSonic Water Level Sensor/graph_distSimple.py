#run in python 3

import RPi.GPIO as GPIO
import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime
from time import sleep, strftime, time
import matplotlib.pyplot as plt     #matplotlib module must be downloaded for py3
import getpass


GPIO.setmode(GPIO.BCM)
print ("Distance Measurement In Progress")

TRIG = 23      #from now on, port 23 we will call TRIG
ECHO = 24      #from now on, port 24 we will call ECHO

GPIO.setup(TRIG,GPIO.OUT)  #sets up pin 23 to trigger a ping sound out!
GPIO.setup(ECHO,GPIO.IN)   #sets up pin 24 to listen for a pong echo in!

GPIO.output(TRIG, False)   #stops any echo from a previous program that might still be going

print ("Waiting For Sensor To Settle")
sleep(1)


plt.ion()

x = []  #placeholders for the graph later on
y = []


def distcheck():  #function to measure distance
  count = 0
   
  while True:
    sleep(0.1)
    GPIO.output(TRIG, True)  #fires a pulse
    sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:  #measure some times
      pulse_start = time()
      
    while GPIO.input(ECHO)==1:
      pulse_end = time()

    sleep(0.01)
    
    pulse_duration = pulse_end - pulse_start  #does the maths

    distance = pulse_duration * 17150   #distance = time * speed of sound

    distance = round(distance, 2)       #rounds distance values off to 2 places

   # print ("Distance:",distance,"cm")                    #adds units to make it look neater
    return(distance)


def send_mail_alert():  #function to send email alert
  to = 'dcuish@gmail.com'
  """
  gmail_user = input("Enter full email eg. RPITime@gmail.com")
  gmail_password = getpass.getpass()
  """
  smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
  smtpserver.ehlo()
  smtpserver.starttls()
  smtpserver.login(gmail_user, gmail_password)


  my_msg=("WARNING! Liquid Level limits exceeded. Disistance at " + str(mode) + "cm")
  msg=MIMEText(my_msg)

  msg['Subject']= 'Flood Warning'
  msg['From']= "Liquid Bot"
  msg['To'] = to
  smtpserver.sendmail(gmail_user, [to], msg.as_string())
  smtpserver.quit()
  print("Email sent to " + str(to))


######################
#program starts here
  #######################


print("Welcome to liquid level meter")
print("Turn on email alert?")
email_choice=input("y/n?")

if email_choice == "y": #choose to turn email alerts on or off
  mailAlert = 1 #on
  print("Mail alerts on")
  limit=input("Set a limit in cm to trigger an email alert eg. 5 ")


  gmail_user = input("Enter full email eg. RPITime@gmail.com")
  gmail_password = getpass.getpass(prompt="Type in your password")

  
elif email_choice == "n":
  print("That's cool.")
  mailAlert = 0 #off

print("Do you want to graph the results?")  #choose to turn graphing on or off
graph_choice=input("y/n?")

datacount = 0 #for no graph mode, a measurement count is handy to know how long
#the sensor has been running. This delcares a variable to count measurments.

while True:

    readings_list = []  #makes an empty list to take the readings

    number_of_readings = 50  #how many readings to take and find the mode of
    
    for pizza in range(number_of_readings):  #takes 10 readings
        distance = distcheck()  #checks distance
        readings_list.append(int(distance)) #puts the 10 values in a list

    print(readings_list) #prints the list and gets the mode (most common value)
    mode = max(set(readings_list), key=readings_list.count)
    print("The mode of " + str(number_of_readings) + " values is " + str(mode))

    if mode <10 and mailAlert == 1:  #sends email if mode is <10cm
      send_mail_alert()
      sleep(5)
      mailAlert = 0 #stops more than one email alert being sent
      
      print("DANGEROUS LEVELS. EMAIL ALERT SENT>>>>>>>>")
      
    #writes this data to a table (a .csv file), this is needed for the graph
    with open("cpu_dists.csv", "a") as log:   # "a" means append to the end
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(mode)))


    if graph_choice == "y":


      #the code below makes the graph and controlls it's settings
        
      days = time()/(60*60*24) #graph shows seconds but we want days 
      
      y.append(mode)   #puts the distance values on the y-axis
      x.append(days)    #puts the distance values on the x-axis
      plt.clf()
      plt.scatter(x,y)    #chooses the scatter plot chart type
      plt.plot(x,y)
      plt.suptitle("Distance over time")  #graph title
      plt.xlabel("Time (Days)")
      plt.ylabel("Distance (cm)")
      plt.draw()          #draws the graph (or if an a loop, updates the graph)

      sleep(0.01)         #Waits between measurements. This could be made longer to save power.

    elif graph_choice == "n":
      datacount=datacount+1
      print("Measurement " + str(datacount))

