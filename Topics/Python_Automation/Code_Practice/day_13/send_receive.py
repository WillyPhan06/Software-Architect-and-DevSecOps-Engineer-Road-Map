import smtplib
from email.mime.text import MIMEText

# Your info
sender_email = "sender@gmail.com"
receiver_email = "receiver@gmail.com"
password = "the password here"

# Email content
subject = "Automation Test"
body = "Hey there! This email was sent using Python automation by Willy."

# Create message
msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

# Connect and send
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)
    server.send_message(msg)

print("Email sent successfully!")
