import requests
from bs4 import BeautifulSoup
import pandas as pd


base_url = "http://books.toscrape.com/catalogue/page-{}.html"

all_books = []

for page in range(1, 6):
    try:  # scrape first 5 pages
        url = base_url.format(page)
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")
        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            all_books.append({"title": title, "price": price})
        print(f"Page {page} scraped successfully.")
    except Exception as e:
        print(f"An error occurred on page {page}: {e}")
        continue

df = pd.DataFrame(all_books)
print(df.head())

df.to_csv("books_multi_page.csv", index=False, encoding='utf-8-sig')
print("Scraped data saved!")



