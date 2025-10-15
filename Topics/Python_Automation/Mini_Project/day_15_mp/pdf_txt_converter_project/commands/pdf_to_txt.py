# TODO: implement pdf_to_txt.py
from .base import Command
from converters.pdf_to_txt import PdfToTxtConverter
from utils.file_manager import FileManager

class PdfToTxtCommand(Command):
    def __init__(self, file_manager, email_sender=None):
        """
        file_manager: FileManager instance
        email_sender: EmailSender instance (optional, can be None if email not used)
        """
        self.file_manager = file_manager
        self.converter = PdfToTxtConverter()
        self.email_sender = email_sender

    def execute(self):
        try:
            # 1. Get input PDF
            pdf_input = input("Enter PDF file name (in pdfs folder) or full path: ").strip()
            pdf_path = self.file_manager.resolve_path(pdf_input, "pdf")
            pdf_path = self.file_manager.categorize_file(pdf_path)

            # 2. Get output TXT name
            txt_output_name = input("Enter output TXT filename (without path, .txt will be added): ").strip()
            if not txt_output_name.lower().endswith(".txt"):
                txt_output_name += ".txt"
            txt_output_path = f"{self.file_manager.txt_folder}/{txt_output_name}"

            # 3. Convert PDF to TXT
            self.converter.convert(pdf_path, txt_output_path)

            # 4. Ask for sending email
            if self.email_sender:
                send = input("Do you want to send this TXT via email? (y/n): ").strip().lower()
                if send == "y":
                    to_email = input("Enter receiver email: ").strip()
                    subject = input("Enter email subject: ").strip()
                    body = input("Enter email body: ").strip()
                    self.email_sender.send_email(subject, body, to_email, txt_output_path)

        except Exception as e:
            print(f"[ERROR] {e}")
