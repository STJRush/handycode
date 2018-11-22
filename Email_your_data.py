import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime
#account info
to = 'example@gmail.com'
gmail_user = 'example@gmail.com'
gmail_password = 'your_password'
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
my_ip='your_message'
msg=MIMEText(my_ip)
msg['Subject']= 'the_subject'
msg['From']= gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
