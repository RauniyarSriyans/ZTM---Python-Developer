# smtp stands for simple mail transfer protocol
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# this html conains the content of the body of the email
html = Template(Path('index.html').read_text())

# creating an email object here
email = EmailMessage()

# the sender is added as a key value pair to the email object
email['from'] = 'Sriyans Rauniyar'
# the receiver is added as a key value pair to the email object
email['to'] = 'rauniyar@princeton.edu'
# the subject is also added as a key value pair to the email object
email['subject'] = 'I am a Python Master'

# the content of the email is also added as a key value pair to the object
email.set_content(html.substitute({'name': 'Shree'}), 'html')

# now, use SMTP protocol to connect to gmail smtp server using port 587 (recommended)
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # SMTP command to tell the server that it is an SMTP client
    smtp.ehlo()
    # start tls which upgrades to a secured layer
    smtp.starttls()
    # login using your email and APP password (remember, not your normal password but your app password)
    smtp.login('sriyansrauniyar21@gmail.com', 'APP PASSWORD HERE')
    # send the email
    smtp.send_message(email)
    print('done!')