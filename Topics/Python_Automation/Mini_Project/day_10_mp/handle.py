import pandas as pd

df = pd.read_csv("sales.csv")
print(df)

df = df.drop(columns=["extra_column"])

df.rename(columns={"units_sold":"Units Sold", "unit_price":"Unit Price", "product":"Product"}, inplace=True)

df = df[df["Units Sold"] > 5]

df["Revenue"] = df["Units Sold"] * df["Unit Price"]

print(df)
