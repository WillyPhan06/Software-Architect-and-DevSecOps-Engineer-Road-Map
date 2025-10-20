import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

# Check response status
if response.status_code == 200:
    data = response.json()
    print("First item:", data[0])
    print("---")
    for i in range(5):
        print(f"Title {i+1}: {data[i]['title']}")
        print(f"Body {i+1}: {data[i]['body']}")
    print("---")
    print(f"Total items fetched: {len(data)}")
else:
    print("Failed to fetch data:", response.status_code)
