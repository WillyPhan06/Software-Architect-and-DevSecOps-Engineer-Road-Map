import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())

url2 = "https://jsonplaceholder.typicode.com/posts"

print("---")

params = {"userId": 1}  # fetch posts by userId = 1

response = requests.get(url2, params=params)
data = response.json()
print(data)

print("---")

print("Number of posts by userId 1:", len(data))

print("---")

params2 = {"userId": 2}

response2 = requests.get(url2, params=params2)
data2 = response2.json()

print("Number of posts by userId 2:", len(data2))
