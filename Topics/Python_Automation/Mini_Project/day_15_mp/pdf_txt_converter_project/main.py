# TODO: implement main.py
from utils.file_manager import FileManager
from utils.email_sender import EmailSender
from settings.settings_manager import SettingsManager

# Commands
from commands.pdf_to_txt import PdfToTxtCommand
from commands.txt_to_pdf import TxtToPdfCommand
from commands.settings import SettingsCommand

class CommandRegistry:
    """
    Registers menu options dynamically.
    """
    def __init__(self):
        self._registry = {}

    def register(self, key: str, description: str, command):
        self._registry[key] = {"description": description, "command": command}

    def execute(self, key: str):
        if key in self._registry:
            self._registry[key]["command"].execute()
        else:
            print("[ERROR] Invalid option!")

    def show_menu(self):
        print("\n--- Main Menu ---")
        for key, value in self._registry.items():
            print(f"{key}. {value['description']}")
        print("q. Quit")


def main():
    # Initialize core managers
    root_folder = "."  # current folder as root
    file_manager = FileManager(root_folder)
    settings_manager = SettingsManager()
    email_sender = EmailSender(settings_manager)

    # Initialize command registry
    registry = CommandRegistry()

    # Register commands
    registry.register("1", "Convert PDF to TXT", PdfToTxtCommand(file_manager, email_sender))
    registry.register("2", "Convert TXT to PDF", TxtToPdfCommand(file_manager, email_sender))
    registry.register("3", "Settings", SettingsCommand(settings_manager))

    # Main loop
    while True:
        registry.show_menu()
        choice = input("Select an option: ").strip().lower()
        if choice == "q":
            print("Goodbye!")
            break
        registry.execute(choice)


if __name__ == "__main__":
    main()
