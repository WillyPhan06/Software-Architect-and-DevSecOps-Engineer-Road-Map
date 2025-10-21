# main.py
from get_crypto_price import CryptoPriceFetcher
from write_spreadsheet import GoogleSheetWriter

def main():
    # Step 1: Fetch crypto data
    fetcher = CryptoPriceFetcher(coins=["bitcoin", "ethereum", "solana"])
    df = fetcher.get_prices()
    df = fetcher.add_timestamp(df)

    print("Fetched data:")
    print(df)

    # Step 2: Write to Google Sheet
    sheet_writer = GoogleSheetWriter(credentials_path="account_credentials.json", sheet_name="Crypto_Prices")
    sheet_writer.write_dataframe(df)

if __name__ == "__main__":
    main()
