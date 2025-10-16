import gspread
from google.oauth2.service_account import Credentials

# Define scope
scope = ["https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive"]

creds = Credentials.from_service_account_file("service_account.json", scopes=scope)
client = gspread.authorize(creds)

# Open your sheet
sheet = client.open("Test_Sheet").sheet1

# Read first row
print(sheet.row_values(1))

# Write to sheet
data = [
    ["Name", "Age", "Country"],
    ["Willy", 21, "Vietnam"],
    ["Alice", 24, "Canada"]
]
sheet.update("A1:C3", data)

print("Google Sheet updated successfully!")
