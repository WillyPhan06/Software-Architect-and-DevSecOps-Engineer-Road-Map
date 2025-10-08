from openpyxl import Workbook

upcoming_path = r"D:\GitHub_Repos\Personal_GitHub_Repos\Software-Architect-and-DevSecOps-Engineer-Road-Map\Topics\Python_Automation\Code_Practice\day_9\employees.xlsx"

wb = Workbook()
ws = wb.active
ws.title = "Employees"
ws.append(["Name", "Age", "Department", "Salary"])
ws.append(["Alice", 25, "HR", 500])
ws.append(["Bob", 30, "IT", 700])
ws.append(["Charlie", 22, "Marketing", 400])
wb.save(upcoming_path)
print(f"Done creating: {upcoming_path}")
