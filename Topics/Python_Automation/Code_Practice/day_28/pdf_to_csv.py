import pdfplumber
import pandas as pd

pdf_path = "sample-tables.pdf"

dataframes = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            df = pd.DataFrame(table[1:], columns=table[0])  # First row = headers
            dataframes.append(df)

if dataframes:
    for idx, df in enumerate(dataframes, start=1):
        df.to_csv(f"table_{idx}.csv", index=False)

else:
    print("⚠️ No tables found — fallback to text extraction.")
