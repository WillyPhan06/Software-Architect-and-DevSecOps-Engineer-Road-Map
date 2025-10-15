# TODO: implement txt_to_pdf.py
from .base import Converter
from fpdf import FPDF

class TxtToPdfConverter(Converter):
    def convert(self, input_path: str, output_path: str):
        """
        Converts a TXT file to a PDF file.
        input_path: path to TXT
        output_path: path to save PDF
        """
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        try:
            with open(input_path, "r", encoding="utf-8") as txt_file:
                for line in txt_file:
                    pdf.multi_cell(0, 10, line)

            pdf.output(output_path)
            print(f"[SUCCESS] Converted TXT to PDF: {output_path}")
        except Exception as e:
            print(f"[ERROR] Failed to convert TXT to PDF: {e}")
