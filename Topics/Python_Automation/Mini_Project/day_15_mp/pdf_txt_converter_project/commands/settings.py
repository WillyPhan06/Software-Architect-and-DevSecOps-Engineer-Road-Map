# TODO: implement settings.py
from .base import Command
from settings.settings_manager import SettingsManager

class SettingsCommand(Command):
    def __init__(self, settings_manager: SettingsManager):
        self.settings_manager = settings_manager

    def execute(self):
        while True:
            print("\n--- Settings Menu ---")
            self.settings_manager.show_settings()
            print("1. Update sender email")
            print("2. Update app password")
            print("3. Update SMTP server")
            print("4. Update SMTP port")
            print("5. Back to main menu")

            choice = input("Choose an option: ").strip()
            if choice == "1":
                email = input("Enter sender email: ").strip()
                self.settings_manager.update_email_settings(email=email)
            elif choice == "2":
                password = input("Enter app password: ").strip()
                self.settings_manager.update_email_settings(app_password=password)
            elif choice == "3":
                smtp_server = input("Enter SMTP server: ").strip()
                self.settings_manager.update_email_settings(smtp_server=smtp_server)
            elif choice == "4":
                try:
                    smtp_port = int(input("Enter SMTP port: ").strip())
                    self.settings_manager.update_email_settings(smtp_port=smtp_port)
                except ValueError:
                    print("[ERROR] Invalid port number.")
            elif choice == "5":
                break
            else:
                print("[ERROR] Invalid choice, try again.")
