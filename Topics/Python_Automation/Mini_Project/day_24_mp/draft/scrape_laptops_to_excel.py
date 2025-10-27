from bs4 import BeautifulSoup
import pandas as pd

# Read your HTML file (replace with your filename)
with open("laptops_page.html", "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

# Find all product cards
products = soup.select("div.card.thumbnail")

data = []

for product in products:
    name = product.select_one("a.title").get_text(strip=True)
    price = product.select_one(".price span").get_text(strip=True)
    details = product.select_one(".description").get_text(strip=True)

    rating = len(product.select(".ratings span.ws-icon-star"))
    reviews = product.select_one(".review-count span").get_text(strip=True)

    data.append({
        "Name": name,
        "Price": price,
        "Details": details,
        "Rating": rating,
        "Number of Reviews": reviews
    })

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("laptops_data.csv", index=False, encoding="utf-8-sig")

print(df)
