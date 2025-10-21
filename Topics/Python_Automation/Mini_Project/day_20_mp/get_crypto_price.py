# get_crypto_price.py
import requests
import pandas as pd
from datetime import datetime

class CryptoPriceFetcher:
    """Handles fetching and formatting crypto prices from the CoinGecko API."""

    def __init__(self, coins=None, currency="usd"):
        self.base_url = "https://api.coingecko.com/api/v3/simple/price"
        self.coins = coins or ["bitcoin", "ethereum", "solana"]
        self.currency = currency

    def fetch(self):
        """Fetch raw JSON data from the API."""
        params = {"ids": ",".join(self.coins), "vs_currencies": self.currency}
        response = requests.get(self.base_url, params=params, timeout=15)
        response.raise_for_status()
        return response.json()

    def to_dataframe(self, data):
        """Convert API data to a clean DataFrame."""
        df = pd.DataFrame(data).T
        df.reset_index(inplace=True)
        df.rename(columns={"index": "coin"}, inplace=True)
        return df

    def get_prices(self):
        """Fetch and return prices as a DataFrame."""
        data = self.fetch()
        df = self.to_dataframe(data)
        return df
    
    def add_timestamp(self, df):
        """Add a timestamp column to the DataFrame."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df["timestamp"] = timestamp
        return df
