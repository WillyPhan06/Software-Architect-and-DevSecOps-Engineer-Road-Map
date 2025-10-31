import pandas as pd
import os

for i in range(1,12):
    df = pd.read_csv(f"table_{i}.csv")

    # Example cleaning
    df.columns = [col.strip().title() for col in df.columns]  # Normalize headers
    df = df.dropna(how="all")  # Drop empty rows

    # Example conversion: if there’s a Price or Amount column
    for col in df.columns:
        if "price" in col.lower() or "amount" in col.lower():
            df[col] = (
                df[col]
                .astype(str)
                .str.replace("$", "")
                .str.replace(",", "")
                .astype(float)
            )

    os.makedirs("cleaned", exist_ok=True)
    df.to_excel(f"cleaned/cleaned_pdf_data_{i}.xlsx", index=False)
    print(f"✅ Cleaned data {i} saved to Excel")
