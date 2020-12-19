import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime
from time import sleep

testdist= 21

#account info

to = 'dcuish@gmail.com'
gmail_user = 'RPiTime@gmail.com'
gmail_password = '12345616'

smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.login(gmail_user, gmail_password)
#today = datetime.date.today()


my_msg="WARNING! Liquid Level limits exceeded. Disistance at " + str(testdist)
msg=MIMEText(my_msg)

msg['Subject']= 'Flood Warning'
msg['From']= "Liquid Bot"
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
print("mail sent")
