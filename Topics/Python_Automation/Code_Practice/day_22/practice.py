import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.w3schools.com/html/html_tables.asp"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
print(html[:500])

table = soup.find("table", {"id": "customers"})  # select table by id
rows = table.find_all("tr")

data = []
for row in rows[1:]:  # skip header
    cols = row.find_all("td")
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Company", "Contact", "Country"])
print(df)
df.to_csv("table_data.csv", index=False)
print("Table saved to CSV")

print("---")

url_ul = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_lists4"
response_ul = requests.get(url_ul)
html_ul = response_ul.text
soup_ul = BeautifulSoup(html_ul, "html.parser")

ul = soup_ul.find("ul")
items = [li.get_text(strip=True) for li in ul.find_all("li")]

print(items)
pd.DataFrame(items, columns=["Item"]).to_csv("list_data.csv", index=False)



