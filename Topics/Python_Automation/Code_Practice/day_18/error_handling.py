import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/invalidendpoint")
    response.raise_for_status()  # raise error if status != 200
except requests.exceptions.HTTPError as e:
    print("HTTP error occurred:", e)
except Exception as e:
    print("Other error:", e)
