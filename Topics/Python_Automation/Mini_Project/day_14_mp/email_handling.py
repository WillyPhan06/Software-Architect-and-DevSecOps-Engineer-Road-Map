from dataclasses import dataclass
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

@dataclass
class Email_Sender:
    smtp_server: str
    port: int
    sender_email: str
    password: str

    def create_message(self, recipient_email: str, subject: str, body: str):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        return msg

    def attach_files(self, msg, files: list):
        for file in files:
            with open(file, 'rb') as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={file}')
            msg.attach(part)

    def send_email(self, recipient_email: str, subject: str, body: str, attachments: list = []):
        msg = self.create_message(recipient_email, subject, body)
        if attachments:
            self.attach_files(msg, attachments)
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.starttls()
            server.login(self.sender_email, self.password)
            server.send_message(msg)