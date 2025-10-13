from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

def send_email_with_attachment(sender, password, receiver, subject, body, filename=None):
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    if filename:
        print(f"Found attachment: {filename}")
        with open(filename, "rb") as f:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(f.read())
            print(f"Attachment {filename} read successfully.")
        encoders.encode_base64(part)
        print(f"Attachment {filename} encoded successfully.")
        part.add_header("Content-Disposition", f"attachment; filename={filename}")
        msg.attach(part)
        print(f"Attachment {filename} attached to email.")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)
        print(f"Email sent to {receiver}.")

    print("Email sent successfully!")

if __name__ == "__main__":
    sender_email = "sender@gmail.com"
    sender_password = "password"
    receiver_email = "receiver@gmail.com"
    subject = "Automated Email with Attachment"
    body = "This is an automated email with an optional attachment."
    attachment_file = "final_report.pdf"  # Set to None if no attachment
    send_email_with_attachment(sender_email, sender_password, receiver_email, subject, body, attachment_file)


