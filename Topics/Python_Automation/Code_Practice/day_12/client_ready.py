import os
from PyPDF2 import PdfMerger

def merge_pdfs(input_folders, output_file):
    merger = PdfMerger()
    for input_folder in input_folders:
        pdf_files = sorted([f for f in os.listdir(input_folder) if f.endswith("8.pdf")])

        if not pdf_files:
            print("⚠️ No PDF files found in", input_folder)
            return

        for pdf in pdf_files:
            print("Merging:", pdf)
            merger.append(os.path.join(input_folder, pdf))

    merger.write(output_file)
    merger.close()
    print(f"Merged {len(pdf_files)} PDFs into '{output_file}'")

if __name__ == "__main__":
    merge_pdfs(["invoices","out_voice"], "final_report_duplicate.pdf")
