import pandas as pd

org_csv_path = r"D:\GitHub_Repos\Personal_GitHub_Repos\Software-Architect-and-DevSecOps-Engineer-Road-Map\Topics\Python_Automation\Mini_Project\day_6_mp\org_employees.csv"
new_csv_path = r"D:\GitHub_Repos\Personal_GitHub_Repos\Software-Architect-and-DevSecOps-Engineer-Road-Map\Topics\Python_Automation\Mini_Project\day_6_mp\updated_employees.csv"

df = pd.read_csv(org_csv_path)

df['Salary'] = [42000,110000,65000]

df = df[df['age']>=25]

df.to_csv(new_csv_path, index=False)