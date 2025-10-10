import PyPDF2

with open("sample_pdf.pdf", "rb") as f:  # rb = read binary
    reader = PyPDF2.PdfReader(f)
    print("Number of pages:", len(reader.pages))

    # Read text from first page
    first_page = reader.pages[0]
    text = first_page.extract_text()
    print(text)
    words = text.split()
    print("Number of words on first page:", len(words))
