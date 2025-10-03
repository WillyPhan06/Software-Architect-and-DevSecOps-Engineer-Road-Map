import pandas as pd

my_csv_path = r"D:\GitHub_Repos\Personal_GitHub_Repos\Software-Architect-and-DevSecOps-Engineer-Road-Map\Topics\Python_Automation\Code_Practice\day_6\my_people.csv"

df = pd.read_csv(my_csv_path)
print(df)

print("This is the head")
print(df.head())

print("These are columns")
print(df.columns)

print("Print info")
print(df.info())

#Mini - Practice
###
# Print just the 'name' column
print(df['Name'])

# Print rows where age > 500
print(df[df[' Age']>500])
###

# Modify or add data
df['Country']=['Malaysia', 'Vietnam']
print("Updated with countries")
print(df)

#Save updated DataFrame to another csv
new_updated_csv_path = r"D:\GitHub_Repos\Personal_GitHub_Repos\Software-Architect-and-DevSecOps-Engineer-Road-Map\Topics\Python_Automation\Code_Practice\day_6\new_people.csv"
df.to_csv(new_updated_csv_path, index=False)

#Read updated csv and modify it more
ndf = pd.read_csv(new_updated_csv_path)
ndf['Job'] = ['Pro Hacker', 'Noob Gamer']
ndf.to_csv(new_updated_csv_path, index=False)

#Get description 
print(ndf.describe())

#Sort rows based on value, this time it's from highest to lowest
print("Below is table sorted from highest age to lowest")
ndf.columns = ndf.columns.str.strip()
ndf_sorted = ndf.sort_values(by='Age', ascending=False)
print(ndf_sorted)