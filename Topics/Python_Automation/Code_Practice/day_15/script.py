import os
from PyPDF2 import PdfReader

pdf_folder = "pdfs"
all_text = ""
unique_word_count = {}

for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        path = os.path.join(pdf_folder, filename)
        reader = PdfReader(path)
        for page in reader.pages:
            for word in page.extract_text().split():
                word = word.lower().strip('.,!?;"()[]{}')
                if word not in unique_word_count:
                    unique_word_count[word] = 0
                unique_word_count[word] += 1
            all_text += page.extract_text() + "\n"

print(all_text)  # preview all chars
print("-------------------------")
print(f"Total unique words: {len(unique_word_count)}")
print("-------------------------")
print(f"Unique words of the word 'the': {unique_word_count['the'] if 'the' in unique_word_count else 0}")
lines = all_text.splitlines()
lines_contain_numbers = [line for line in lines if any(char.isdigit() for char in line)]
print("-------------------------")
print(f"Lines containing numbers: {len(lines_contain_numbers)}")

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(all_text)
    print("All text written to output.txt")

with open("lines_with_numbers.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines_contain_numbers))
    print("Lines with numbers written to lines_with_numbers.txt")