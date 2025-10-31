import pdfplumber
import pandas as pd

pdf_path = "sample-tables.pdf"
all_text = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            all_text.append(text)

# Join all text for now
pdf_data = "\\n".join(all_text)

print("✅ PDF text extracted successfully!")
print(pdf_data[:500])  # Preview first 500 chars
