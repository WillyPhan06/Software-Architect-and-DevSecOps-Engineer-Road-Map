from PyPDF2 import PdfMerger
import os
import sys

def merge_pdfs(pdfs, output_path, pdf_folders=None):
    merger = PdfMerger()

    if isinstance(pdfs, str):
        pdfs = [pdfs]

    if isinstance(pdf_folders, str):
        pdf_folders = [pdf_folders]

    if pdf_folders:
        for folder in pdf_folders:
            for pdf in os.listdir(folder):
                if pdf.endswith('.pdf') and pdf in pdfs:
                    merger.append(os.path.join(folder, pdf))
    

    merger.write(output_path)
    merger.close()

    return output_path

def main():
    while True:
        ini_choice = input("Enter folders you wanna merge PDFs from (comma-separated) or 'n' to skip or 'q' to quit: ")
        if ini_choice.lower() == 'n':
            print("Skipping folder input.")
            pdf_folders = None
        elif ini_choice.lower() == 'q':
            print("Exiting program.")
            sys.exit(0)
        else:
            pdf_folders = [folder.strip() for folder in ini_choice.split(',')]
            if all(os.path.isdir(folder) for folder in pdf_folders):
                print("All folders exist.")
            else:
                print("One or more folders do not exist. Please try again.")
                continue
        second_choice = input("Enter individual PDF files to merge (comma-separated) or 'n' to skip or 'q' to quit: ")
        if second_choice.lower() == 'n':
            print("Skipping individual PDF input.")
            pdfs = None
            sys.exit(0)
        elif second_choice.lower() == 'q':
            print("Exiting program.")
            sys.exit(0)
        else:
            pdfs = [pdf.strip() for pdf in second_choice.split(',')]
            
            if all(pdf.endswith('.pdf') for pdf in pdfs):
                print("All PDF files validated.")
                
            else:
                print("One or more PDF files do not exist or are not PDFs. Please try again.")
                continue

        output_path = input("Enter the output PDF file path (e.g., output.pdf): ").strip()
        if not output_path.endswith('.pdf'):
            print("Output file must have a .pdf extension. Please try again.")
            continue
        try:
            merge_pdfs(pdfs, output_path, pdf_folders)
            print(f"Merged PDFs saved to {output_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

if __name__ == "__main__":
    main()

        
