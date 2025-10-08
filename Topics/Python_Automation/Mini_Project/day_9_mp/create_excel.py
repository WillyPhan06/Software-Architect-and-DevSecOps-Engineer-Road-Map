from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
import random

# Create workbook and worksheet
wb = Workbook()
ws = wb.active
ws.title = "Employees"

# Header row
header = ["Name", "Age", "Department", "Salary", "Country", "Sex"]
ws.append(header)

# Style the header
for cell in ws[1]:
    cell.font = Font(bold=True)
    cell.alignment = Alignment(horizontal="center", vertical="center")

# Sample data pools
first_names = ["John", "Emma", "Liam", "Olivia", "Noah", "Ava", "Ethan", "Sophia"]
last_names = ["Smith", "Johnson", "Brown", "Taylor", "Lee", "Martinez", "Garcia", "Kim"]
departments = ["HR", "IT", "Marketing", "Finance", "Operations"]
countries = ["USA", "UK", "Germany", "Vietnam", "Canada"]
sexes = ["M", "F"]

# Generate 20 rows of random data
for _ in range(20):
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    age = random.randint(22, 60)
    department = random.choice(departments)
    salary = round(random.uniform(3000, 12000), 2)
    country = random.choice(countries)
    sex = random.choice(sexes)

    ws.append([name, age, department, salary, country, sex])

# Save the file
wb.save(r"D:\GitHub_Repos\Personal_GitHub_Repos\Software-Architect-and-DevSecOps-Engineer-Road-Map\Topics\Python_Automation\Mini_Project\day_9_mp\employee_data.xlsx")

print("Generated successfully!")
