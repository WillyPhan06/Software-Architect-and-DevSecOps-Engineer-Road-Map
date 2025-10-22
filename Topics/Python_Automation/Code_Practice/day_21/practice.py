import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://dantri.com.vn/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}
response = requests.get(url, headers=headers)

print(response.status_code)  # 200 means success
html = response.text
# print(html[:2000])  # Print the first 500 characters of the HTML

soup = BeautifulSoup(html, "html.parser")

# Example: find all headline elements
headlines = soup.find_all("h2")

for h in headlines[:10]:
    print(h.get_text(strip=True))

data = []
for h in headlines[:10]:
    title = h.get_text(strip=True)
    data.append({"headline": title})

df = pd.DataFrame(data)
df.to_csv("headlines.csv", index=False)
print("Saved 10 headlines to headlines.csv")

print("---")

for tag in soup.find_all("a", limit=10):
    print(tag.get_text(strip=True), "→", tag.get("href"))



