from bs4 import BeautifulSoup

def parse_laptops(html: str) -> list[dict]:
    """Extract laptop info from one HTML page."""
    soup = BeautifulSoup(html, "html.parser")
    products = soup.select("div.card.thumbnail")

    data = []
    for product in products:
        try:
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
        except Exception as e:
            print(f"⚠️ Error parsing product: {e}")
            continue

    return data
