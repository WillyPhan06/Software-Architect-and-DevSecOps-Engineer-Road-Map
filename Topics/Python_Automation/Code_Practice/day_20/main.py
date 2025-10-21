# main.py

import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/simple/price"
params = {"ids": "bitcoin,ethereum,solana", "vs_currencies": "usd"}

response = requests.get(url, params=params)
data = response.json()

print(data)

print("---")

df = pd.DataFrame(data).T  # transpose to have coins as rows
df.reset_index(inplace=True)
df.rename(columns={"index": "coin"}, inplace=True)

print(df)