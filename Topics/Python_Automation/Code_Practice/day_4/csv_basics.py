import csv

people_file = r"D:\GitHub_Repos\Personal_GitHub_Repos\Software-Architect-and-DevSecOps-Engineer-Road-Map\Topics\Python_Automation\Code_Practice\day_4\people.csv"

with open(people_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name","Age","Location"])
    writer.writerow(["Willy",100,"HCMC"])
    writer.writerow(["Nora", 20, "HCMC"])

with open(people_file,"r") as f_2:
    reader = csv.reader(f_2)
    for row in reader:
        print(row)

