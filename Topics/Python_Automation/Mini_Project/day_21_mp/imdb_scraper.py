import requests
from bs4 import BeautifulSoup
import pandas as pd

# IMDb Top 250 URL
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"


# Use headers to pretend we're a normal browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.google.com/",
}


# Fetch the page
response = requests.get(url, headers=headers)

# Check if the connection was successful
if response.status_code != 200:
    print(f"Failed to retrieve page, status code: {response.status_code}")
    exit()

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all movie containers
movies = soup.select("li.ipc-metadata-list-summary-item")

# Prepare lists to store data
titles, years, ratings = [], [], []

for movie in movies:
    # Title
    title_tag = movie.select_one("h3")
    title = title_tag.get_text(strip=True) if title_tag else "N/A"

    # Year
    year_tag = movie.select_one("span.sc-b189961a-8")
    year = year_tag.get_text(strip=True) if year_tag else "N/A"

    # Rating
    rating_tag = movie.select_one("span.ipc-rating-star--rating")
    rating = rating_tag.get_text(strip=True) if rating_tag else "N/A"

    titles.append(title)
    years.append(year)
    ratings.append(rating)

# Create a DataFrame
df = pd.DataFrame({
    "Title": titles,
    "Year": years,
    "Rating": ratings
})

# Save to CSV
df.to_csv("imdb_top_250.csv", index=False, encoding="utf-8-sig")

print("Scraping complete! Saved to imdb_top_250.csv")
