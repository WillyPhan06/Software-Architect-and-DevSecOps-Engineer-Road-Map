import requests
import pandas as pd
from practice import data

df = pd.DataFrame(data)
print(df.head())

print("---")

# Optional: select only certain columns
df_selected = df[["userId", "id", "title"]]
print(df_selected.head())

print("---")

df_filter_id_1 = df[df["userId"] == 1]
print(df_filter_id_1)
print(f"Sigma len: {len(df_filter_id_1)}")

print("---")

count = 1
while df[df["userId"] == count].empty is False:
    df_user = df[df["userId"] == count]
    print(f"UserId {count} has {len(df_user)} items")
    count += 1

print("---")

# Save to CSV
df_selected.to_csv("posts.csv", index=False)

# Save to Excel
df_selected.to_excel("posts.xlsx", index=False)
print("Data saved locally")

