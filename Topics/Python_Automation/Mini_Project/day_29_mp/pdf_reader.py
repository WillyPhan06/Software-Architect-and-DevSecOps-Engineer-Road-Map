import pdfplumber
import logging
import os
from datetime import datetime

# Setup logging
logging.basicConfig(filename="process.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

PDF_PATH = "sample.pdf"

def read_pdf(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"PDF file not found: {path}")

    with pdfplumber.open(path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def main():
    try:
        logging.info("Starting PDF read operation...")
        text = read_pdf(PDF_PATH)
        logging.info(f"Successfully read {len(text)} characters from PDF.")
    except Exception as e:
        logging.error(f"Error reading PDF: {e}")

if __name__ == "__main__":
    main()
