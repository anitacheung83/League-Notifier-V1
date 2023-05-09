import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def send_email(recipient: str):
    msg = MIMEMultipart()
    msg['Subject'] = 'Weekly Report'
    msg['From'] = ""
    msg['To'] = recipient
