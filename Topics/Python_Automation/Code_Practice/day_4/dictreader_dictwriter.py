import csv
import time

people2_file = r"D:\GitHub_Repos\Personal_GitHub_Repos\Software-Architect-and-DevSecOps-Engineer-Road-Map\Topics\Python_Automation\Code_Practice\day_4\people2.csv"

# Writing with DictWriter
with open(people2_file, "w", newline="") as f:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name": "Charlie", "Age": 22, "City": "Da Nang"})

time.sleep(1)

# Reading with DictReader
with open(people2_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["City"])
