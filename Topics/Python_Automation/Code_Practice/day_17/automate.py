import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

# Define scopes
scope = ["https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive"]

# Authenticate
creds = Credentials.from_service_account_file("service_account.json", scopes=scope)
client = gspread.authorize(creds)

# Open your sheet
sheet = client.open("Test_Sheet").sheet1

print(sheet.title)

print("---")

print(sheet.row_values(1))

print("---")

# Get all data
data = sheet.get_all_records()  # returns list of dictionaries
print(data)

print("---")

# Convert to Pandas DataFrame
df = pd.DataFrame(data)
print(df.head())

# Update single cell
sheet.update("D1", [["Products Sold"]])

# Update multiple cells using a list of lists
values = [
    [25],
    [50]
]
sheet.update("D2:D3", values)

print("---")

# Get all data
data2 = sheet.get_all_records()  # returns list of dictionaries
print(data2)

print("---")

# Convert to Pandas DataFrame
df2 = pd.DataFrame(data2)
print(df2.head())

print("---")
# Filter rows
filtered_df = df2[df2["Products Sold"] > 35]

# Show filtered data
print(filtered_df)

sheet.append_row(["Monitor", 5, "Hawaii", 300])


# Write entire DataFrame to Sheet
df2["Revenue"] = df2["Products Sold"] * df2["Age"]

sheet.clear()

# Convert DataFrame to list of lists (including header)
data_to_write = [df2.columns.values.tolist()] + df2.values.tolist()
sheet.update("A1", data_to_write)




