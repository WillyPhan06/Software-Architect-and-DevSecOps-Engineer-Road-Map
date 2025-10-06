import pandas as pd

csv_path = r"D:\GitHub_Repos\Personal_GitHub_Repos\Software-Architect-and-DevSecOps-Engineer-Road-Map\Topics\Python_Automation\Code_Practice\day_7\employees.csv"

df = pd.read_csv(csv_path)
# print(df)

# Rename single column
df.rename(columns={"fullname": "name"}, inplace=True)

# Rename multiple
df.rename(columns={"salary": "monthly_salary", "department": "dept"}, inplace=True)

df.rename(columns={"age": "y/o"}, inplace=True)

df = df.drop(columns=["extra"])

df = df.drop(columns=["id"])

df = df.drop(index=2)


print(df.head())

print("--------------------------------")

print(df[df["name"]=="Bob Tran"]["monthly_salary"])

print("--------------------------------")

print(df[(df["dept"] == "IT") & (df["monthly_salary"]<675)])

print("--------------------------------")

print(df[df["dept"].isin(["IT"])])

print("--------------------------------")

my_row = df.iloc[1]
print(my_row)


