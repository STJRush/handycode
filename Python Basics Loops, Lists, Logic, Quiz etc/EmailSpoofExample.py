# code from https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151
# email spoof example

import smtplib
import ssl
from email.message import EmailMessage

# Define email sender and receiver
email_sender = 'rpitime@gmail.com'
email_password = 'enter your pw here'
email_receiver = 'nicola.testla@stjosephsrush.com'

# Set the subject and body of the email
subject = 'YOU HAVE BEEN HACKED'
body = """
This is how easy it is to spoof email sender using a python script.
"""

em = EmailMessage()
em['From'] = "Mr. Nealon"
em['To'] = "MrMurrayAllCurry"
em['Subject'] = subject
em.set_content(body)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
