import pandas as pd

# Step 1: Read the messy Excel
df = pd.read_excel("super_messy_data.xlsx")

print("Original messy data:")
print(df)

# Step 2: Clean string columns
str_cols = ["Product", "Notes", "Extra"]
for col in str_cols:
    if col in df.columns:
        df[col] = df[col].astype(str)                  # convert everything to string first
        df[col] = df[col].str.strip()                  # remove leading/trailing spaces
        df[col].replace({"None": "", "nan": ""}, inplace=True)  # clean literal 'None'

# Step 3: Clean numeric columns
num_cols = ["Units Sold", "Unit Price", "Revenue"]
for col in num_cols:
    if col in df.columns:
        # Convert numeric-looking strings to numbers, invalid -> NaN
        df[col] = pd.to_numeric(df[col], errors="coerce")
        # Fill NaN with 0
        df[col].fillna(0, inplace=True)

# Step 4: Recalculate Revenue for sanity
df["Revenue"] = df["Units Sold"] * df["Unit Price"]

# Step 5: Optional: fix empty product names
df["Product"].replace("", "Unknown", inplace=True)

print("\nCleaned data:")
print(df)

# Step 6: Save cleaned Excel
df.to_excel("cleaned_sales.xlsx", index=False)
print("\nCleaned Excel saved as 'cleaned_sales.xlsx'")
