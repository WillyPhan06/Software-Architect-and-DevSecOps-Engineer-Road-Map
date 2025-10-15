# TODO: implement pdf_to_txt.py
from .base import Converter
import PyPDF2

class PdfToTxtConverter(Converter):
    def convert(self, input_path: str, output_path: str):
        """
        Converts a PDF file to a TXT file.
        input_path: path to PDF
        output_path: path to save TXT
        """
        text = ""
        try:
            with open(input_path, "rb") as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                for page in reader.pages:
                    text += page.extract_text() + "\n"

            with open(output_path, "w", encoding="utf-8") as txt_file:
                txt_file.write(text)
            print(f"[SUCCESS] Converted PDF to TXT: {output_path}")
        except Exception as e:
            print(f"[ERROR] Failed to convert PDF to TXT: {e}")
