import os
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from flask_mail import Message
from flask import current_app
from app.db import get_email_list


EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


curr_dir = os.path.dirname(os.path.abspath(__file__))

from app import mail

# function for reading the message template ie message.txt
def read_template():
    peth = curr_dir + "/messages/message.txt"
    with open(peth, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

# names, emails = get_contacts('mycontacts.txt') 

# function to generate and send mail
def send_welcome_mail(name, email):
    message_template = read_template()

    msg = MIMEMultipart()
    message = message_template.substitute(PERSON_NAME=name.title())

    msg['Subject'] = 'NEWSLETTER SUBSCRIPTION'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email

    msg.attach(MIMEText(message, 'plain'))

    with open(curr_dir + '/messages/smiley.jpg', 'rb') as f:
        file_data = f.read()
        file_name = f.name

    img = MIMEImage(file_data, _subtype="jpg")
    img.add_header('Content-Disposition', 'attachment; filename="%s"' % file_name)
    msg.attach(img)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    del msg

def send_batch_emails(emailcontent):

    subscribers = get_email_list()
    
    
    print(len(subscribers))
    
    # for sub in subscribers:
    #     msg = MIMEMultipart()
    #     msg['Subject'] = emailcontent["subject"]
    #     msg['From'] = EMAIL_ADDRESS
    #     msg['To'] = sub["email"]
        
    #     msg.attach(MIMEText( emailcontent["textContent"], 'plain'))

    #     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #         smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    #         smtp.send_message(msg)
    #     del msg
    
    return True