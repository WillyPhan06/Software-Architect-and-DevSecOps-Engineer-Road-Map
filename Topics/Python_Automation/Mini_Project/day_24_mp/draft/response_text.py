import requests

url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=1"
file_path = "response_text.txt"


def get_response_text(url):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
    
def upload_to_txt(file_path, text):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)
    except IOError as e:
        print(f"Error writing to {file_path}: {e}")
    
if __name__ == "__main__":
    text = get_response_text(url)

    if text:
        upload_to_txt(file_path, text)
        print("Successfully fetched response text.")
    else:
        print("Failed to fetch response text.")