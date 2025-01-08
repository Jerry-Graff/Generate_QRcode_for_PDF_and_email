"""
This script sends an email with an attached QR code image. 

It performs the following steps:
1. Loads SMTP and email configuration from environment variables (or uses hard-coded values).
2. Constructs an email message with a subject, body, and an attachment (QR code image).
3. Connects to the specified SMTP server using TLS, logs in with provided credentials,
   and sends the email to the designated recipient.

Configuration variables used:
- SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD: SMTP server credentials.
- SENDER: The email address sending the email.
- RECIPIENT: The destination email address.
- SUBJECT: The subject line of the email.
- BODY: The plain text body of the email.

Ensure the QR code image file (e.g., 'cv_qr.png') exists in the script's directory before sending.
"""

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


def send_email():
    # SMTP credentials - make sure they are set up with email provider
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")

    # Email send credentials
    sender = os.getenv("SENDER")
    recipient = os.getenv("RECIPIENT")
    subject = os.getenv("SUBJECT")
    body = os.getenv("BODY")

    # Email configuartion
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attach the QR code image
    filename = "cv_qr.png"
    with open(filename, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={filename}')
    msg.attach(part)

    # Send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(sender, recipient, msg.as_string())
    print("Email sent successfully.")
