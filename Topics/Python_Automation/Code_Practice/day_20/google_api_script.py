# google_api_script.py
import gspread
from google.oauth2.service_account import Credentials
from main import df

# Google Sheets auth
creds = Credentials.from_service_account_file("token_credentials.json")

scoped_creds = creds.with_scopes([
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
])

client = gspread.authorize(scoped_creds)

# Open or create sheet
sheet = client.open("Crypto_Prices").sheet1
sheet.clear()
sheet.update([df.columns.values.tolist()] + df.values.tolist())
print("Google Sheet updated!")
