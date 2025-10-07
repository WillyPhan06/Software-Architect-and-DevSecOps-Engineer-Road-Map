from openpyxl import Workbook
import os

xlsx_path_old = r"D:\GitHub_Repos\Personal_GitHub_Repos\Software-Architect-and-DevSecOps-Engineer-Road-Map\Topics\Python_Automation\Code_Practice\day_8\employees.xlsx"
xlsx_path_new = r"D:\GitHub_Repos\Personal_GitHub_Repos\Software-Architect-and-DevSecOps-Engineer-Road-Map\Topics\Python_Automation\Code_Practice\day_8\staff.xlsx"

# Renaming the file, plugging in old path and new path for os to rename them
os.rename(xlsx_path_old, xlsx_path_new)

# Create a new workbook
wb = Workbook()

# Select the active sheet
ws = wb.active
ws.title = "Staff"

# Add data
ws.append(["Name", "Age", "Department", "Salary"])
ws.append(["Alice", 25, "HR", 500])
ws.append(["Bob", 30, "IT", 700])
ws.append(["Charlie", 22, "Marketing", 400])
ws.append(["Billiers", 19, "IT", 1000])
ws.append(["Willy", 19, "Computing", 10000])

# Save file
wb.save(xlsx_path_new)

print("Done 1")





