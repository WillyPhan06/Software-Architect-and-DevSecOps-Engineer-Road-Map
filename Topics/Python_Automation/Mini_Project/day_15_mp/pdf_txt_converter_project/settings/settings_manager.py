# TODO: implement settings_manager.py
class SettingsManager:
    def __init__(self):
        # Default settings (Gmail)
        self.email = None
        self.app_password = None
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

    def update_email_settings(self, email: str = None, app_password: str = None,
                              smtp_server: str = None, smtp_port: int = None):
        """
        Update the email and SMTP settings. Only update if value is provided.
        """
        if email:
            self.email = email
        if app_password:
            self.app_password = app_password
        if smtp_server:
            self.smtp_server = smtp_server
        if smtp_port:
            self.smtp_port = smtp_port
        print("[INFO] Settings updated successfully.")

    def get_settings(self):
        """
        Return current settings as dict.
        """
        return {
            "email": self.email,
            "app_password": "******" if self.app_password else None,  # hide password
            "smtp_server": self.smtp_server,
            "smtp_port": self.smtp_port
        }

    def show_settings(self):
        """
        Nicely print current settings (hide password)
        """
        print("Current Email Settings:")
        print(f"  Email: {self.email}")
        print(f"  App Password: {'******' if self.app_password else None}")
        print(f"  SMTP Server: {self.smtp_server}")
        print(f"  SMTP Port: {self.smtp_port}")
