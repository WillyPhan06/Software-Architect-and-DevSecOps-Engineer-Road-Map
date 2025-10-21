# write_spreadsheet.py
import gspread
from google.oauth2.service_account import Credentials

class GoogleSheetWriter:
    """Handles writing pandas DataFrames to Google Sheets."""

    def __init__(self, credentials_path, sheet_name):
        self.credentials_path = credentials_path
        self.sheet_name = sheet_name
        self.client = self._authorize()

    def _authorize(self):
        """Authorize with Google Sheets API."""
        creds = Credentials.from_service_account_file(self.credentials_path)
        scoped_creds = creds.with_scopes([
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ])
        return gspread.authorize(scoped_creds)

    def write_dataframe(self, df):
        """Write the given DataFrame to the configured Google Sheet."""
        sheet = self.client.open(self.sheet_name).sheet1
        sheet.clear()
        sheet.update([df.columns.values.tolist()] + df.values.tolist())
        print(f"Google Sheet '{self.sheet_name}' updated successfully!")
