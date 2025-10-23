import csv

data = [
    {"id": 1, "name": "Alice", "private": False},
    {"id": 2, "name": "Bob", "private": True},
    {"id": 3, "name": "Charlie", "private": False},
    {"id": 4, "name": "David", "private": True},
    {"id": 5, "name": "Eve", "private": False},
]

with open("data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "private"])
    writer.writeheader()
    for row in data:
        writer.writerow(row)
