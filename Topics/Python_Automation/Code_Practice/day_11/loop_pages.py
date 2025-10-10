import PyPDF2

all_text = ""
with open("many_pages.pdf", "rb") as f:
    reader = PyPDF2.PdfReader(f)
    for page in reader.pages:
        all_text += page.extract_text() + "\n"

print(all_text[:500])  # print first 500 chars

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("----------------------------------")

heres = []

print("THEY WERE HERE: ")
lines = all_text.split("\n")
for line in lines:
    if "here" in line:
        heres.append(line)
        print(line)

print(f"Total lines with 'here': {len(heres)}")
