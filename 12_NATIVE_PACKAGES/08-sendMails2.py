from email.mime.multipart import MIMEMultipart  # To Mails
from email.mime.text import MIMEText  # To text body from mails
from email.mime.image import MIMEImage  # To attach images
from pathlib import Path  # To locate the directories
import smtplib  # To localserver from mails

# Multipurpose
# Internet
# Mail
# Extension

path = Path("12_NATIVE_PACKAGES/photo.png")  # Route
mime_image = MIMEImage(path.read_bytes())  # Attach image
msj = MIMEMultipart()
msj["from"] = "User Name"
msj["to"] = "your_mail@gmail.com"
msj["subject"] = "Test Send"
bodyMail = MIMEText("Body Mail")
msj.attach(bodyMail)
msj.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  # Required identifier
    smtp.starttls()  # Encrypted requiered
    # Login in to the Google Server
    smtp.login("you_mail@gmail.com", "your_password")
    smtp.send_message(msj)
    print("Mail Send")
