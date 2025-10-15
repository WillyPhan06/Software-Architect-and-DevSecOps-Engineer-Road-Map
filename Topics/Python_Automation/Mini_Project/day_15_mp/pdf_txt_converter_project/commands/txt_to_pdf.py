# TODO: implement txt_to_pdf.py
from .base import Command
from converters.txt_to_pdf import TxtToPdfConverter
from utils.file_manager import FileManager

class TxtToPdfCommand(Command):
    def __init__(self, file_manager, email_sender=None):
        """
        file_manager: FileManager instance
        email_sender: EmailSender instance (optional)
        """
        self.file_manager = file_manager
        self.converter = TxtToPdfConverter()
        self.email_sender = email_sender

    def execute(self):
        try:
            # 1. Get input TXT
            txt_input = input("Enter TXT file name (in txts folder) or full path: ").strip()
            txt_path = self.file_manager.resolve_path(txt_input, "txt")
            txt_path = self.file_manager.categorize_file(txt_path)

            # 2. Get output PDF name
            pdf_output_name = input("Enter output PDF filename (without path, .pdf will be added): ").strip()
            if not pdf_output_name.lower().endswith(".pdf"):
                pdf_output_name += ".pdf"
            pdf_output_path = f"{self.file_manager.pdf_folder}/{pdf_output_name}"

            # 3. Convert TXT to PDF
            self.converter.convert(txt_path, pdf_output_path)

            # 4. Ask for sending email
            if self.email_sender:
                send = input("Do you want to send this PDF via email? (y/n): ").strip().lower()
                if send == "y":
                    to_email = input("Enter receiver email: ").strip()
                    subject = input("Enter email subject: ").strip()
                    body = input("Enter email body: ").strip()
                    self.email_sender.send_email(subject, body, to_email, pdf_output_path)

        except Exception as e:
            print(f"[ERROR] {e}")
