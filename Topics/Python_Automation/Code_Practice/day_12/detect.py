import os
from PyPDF2 import PdfMerger

merger = PdfMerger()
folder_path = "invoices"

for file in os.listdir(folder_path):
    if file.endswith(".pdf"):
        merger.append(os.path.join(folder_path, file))

merger.write("merged_auto.pdf")
merger.close()

print(" All PDFs in 'invoices/' merged successfully.")
