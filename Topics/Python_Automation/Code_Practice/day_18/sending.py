import requests

url = "https://jsonplaceholder.typicode.com/posts"


for i in range(3):
    payload = {"title": "Bye World", "body": "My first post", "userId": i+1}
    response = requests.post(url, json=payload)
    print("Status Code:", response.status_code)
    print("Response:", response.json())



