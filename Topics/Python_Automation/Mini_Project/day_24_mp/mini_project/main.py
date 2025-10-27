from scraper.fetcher import fetch_page
from scraper.parser import parse_laptops
from scraper.saver import save_to_csv
from scraper.utils import parse_page_input

def main():
    print("=== Laptop Scraper ===")
    user_pages = input("Enter page numbers (e.g. 1-5,8,10): ").strip()
    exclude = input("Exclude pages? (optional, e.g. 3,6): ").strip()
    pages = parse_page_input(user_pages, exclude)

    print(f"➡️  Scraping pages: {pages}")
    all_data = []

    for page in pages:
        html = fetch_page(page)
        if not html:
            continue
        page_data = parse_laptops(html)
        all_data.extend(page_data)

    save_to_csv(all_data, filename="laptops_data.csv", append=False)
    print("🎉 Done!")

if __name__ == "__main__":
    main()
