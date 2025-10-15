# TODO: implement email_sender.py
import smtplib
import os
from email.message import EmailMessage

class EmailSender:
    def __init__(self, settings_manager):
        """
        settings_manager: object that provides email, app_password, smtp_server, smtp_port
        """
        self.settings_manager = settings_manager

    def send_email(self, subject, body, to_email, attachment_path=None):
        email = self.settings_manager.email
        password = self.settings_manager.app_password
        smtp_server = self.settings_manager.smtp_server
        smtp_port = self.settings_manager.smtp_port

        if not email or not password:
            print("[ERROR] Sender email or app password not set. Use settings menu to configure.")
            return False

        msg = EmailMessage()
        msg["From"] = email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.set_content(body)

        # Attach file if given
        if attachment_path:
            try:
                with open(attachment_path, "rb") as f:
                    file_data = f.read()
                    file_name = os.path.basename(attachment_path)
                    msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)
            except Exception as e:
                print(f"[ERROR] Failed to attach file: {e}")
                return False

        # Send email
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(email, password)
                server.send_message(msg)
            print(f"[SUCCESS] Email sent to {to_email}")
            return True
        except Exception as e:
            print(f"[ERROR] Failed to send email: {e}")
            return False
