from PyPDF2 import PdfMerger

merger = PdfMerger()

pdfs = ["w6.pdf", "w7.pdf", "w8.pdf"]

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()

print("Merged all PDFs into 'merged.pdf'")

reversed_merger = PdfMerger()

for pdf in pdfs[::-1]:
    reversed_merger.append(pdf)

reversed_merger.write("reversed_merged.pdf")
reversed_merger.close()

print("Merged all PDFs in reverse order into 'reversed_merged.pdf'")

