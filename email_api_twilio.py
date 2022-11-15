import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from credentials import SENDGRID_API_KEY

message = Mail(
    from_email='anubhavpatrick@gmail.com',
    to_emails='anubhav.patrick@giindia.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
