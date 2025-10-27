import os
import time
import requests

BASE_URL = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={}"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; scraping-project/1.0)"}


def fetch_page(page_num: int, save_html: bool = True, delay: float = 1.0) -> str:
    """Fetch a single page and optionally save the HTML to /data/raw_html/."""
    url = BASE_URL.format(page_num)
    print(f"🌐 Fetching page {page_num}: {url}")

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        html = response.text

        if save_html:
            os.makedirs("data/raw_html", exist_ok=True)
            filename = f"data/raw_html/page_{page_num}.html"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"💾 Saved raw HTML: {filename}")

        time.sleep(delay)
        return html
    except requests.RequestException as e:
        print(f"⚠️ Failed to fetch page {page_num}: {e}")
        return ""
