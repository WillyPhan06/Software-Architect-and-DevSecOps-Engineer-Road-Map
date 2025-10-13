import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender_email = "sender@gmail.com"
receiver_email = "receiver@gmail.com"
password = "the password here"

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Your merged report"

body = "Hey! Attached is your automated report."
msg.attach(MIMEText(body, "plain"))

filename = "final_report.pdf"  # file to attach

with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)
part.add_header("Content-Disposition", f"attachment; filename= {filename}")
msg.attach(part)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)
    server.send_message(msg)

print("Email with attachment sent!")
