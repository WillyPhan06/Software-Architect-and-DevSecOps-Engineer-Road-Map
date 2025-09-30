# Mini project of reading a json file then take the headers and info then pass into the csv then read it and print it out

import json
import csv
import time

json_file = r"D:\GitHub_Repos\Personal_GitHub_Repos\Software-Architect-and-DevSecOps-Engineer-Road-Map\Topics\Python_Automation\Mini_Project\day_4_mp\sample.json"
csv_file = r"D:\GitHub_Repos\Personal_GitHub_Repos\Software-Architect-and-DevSecOps-Engineer-Road-Map\Topics\Python_Automation\Mini_Project\day_4_mp\my_people.csv"

with open(json_file,"r") as jsf:
    ppl = json.load(jsf)

time.sleep(0.5)

header = []

for person in ppl:
    for key in person:
        header.append(key) 
    break

time.sleep(0.5)

with open(csv_file, "w", newline="") as csvf:
    writer = csv.DictWriter(csvf, fieldnames=header)
    writer.writeheader()
    for person in ppl:
        writer.writerow(person)

time.sleep(0.5)

with open(csv_file, "r") as csvf_read:
    reader = csv.DictReader(csvf_read)
    for row in reader:
        print(row["name"], row["age"])









