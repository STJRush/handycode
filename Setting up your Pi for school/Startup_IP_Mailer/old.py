import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime
#account info
to = 'dublinscience@gmail.com'
gmail_user = 'dd'
gmail_password = 'dd'
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()
arg='ip route list'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data=p.communicate()
split_data=data[0].split()
ipaddr=split_data[split_data.index('src')+1]
my_ip='Good day human overlord. This is your humble pi. My ip today is %s' % ipaddr
msg=MIMEText(my_ip)
msg['Subject']= 'Rpi2 Reporting in!'
msg['From']= gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
