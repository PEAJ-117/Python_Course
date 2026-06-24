from email.mime.multipart import MIMEMultipart  # To Mails
from email.mime.text import MIMEText  # To text body from mails
from email.mime.image import MIMEImage  # To attach images
from pathlib import Path  # To locate the directories
from string import Template  # Remplace variables
import smtplib  # To localserver from mails

# Refactor
# tempHtml = """
#     <b>Hola $user</b>
# """

# Import HTML
tempHtml = Path("12_NATIVE_PACKAGES/09-01-template.html").read_text("utf-8")
template = Template(tempHtml)
# bodyY = template.substitute({"user": "Paul Edwin"})  # Remplace variables
bodyY = template.substitute(user="Paul de la Madrid")


path = Path("12_NATIVE_PACKAGES/photo.png")  # Route
mime_image = MIMEImage(path.read_bytes())  # Attach image
msj = MIMEMultipart()
msj["from"] = "User Name"
msj["to"] = "your_mail@gmail.com"
msj["subject"] = "Test Send"
# bodyMail = MIMEText("Contenido del mensaje")
bodyMail = MIMEText(bodyY, "html")
msj.attach(bodyMail)
msj.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  # Required identifier
    smtp.starttls()  # Encrypted requiered
    # Login in to the Google Server
    smtp.login("you_mail@gmail.com", "your_password")
    smtp.send_message(msj)
    print("Mail Send")
