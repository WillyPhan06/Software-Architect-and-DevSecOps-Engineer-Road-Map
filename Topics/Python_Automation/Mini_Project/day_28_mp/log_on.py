# Change log_file to be able to work on your computer, the one below works on mine, it's absolute path

import csv
import os
from datetime import datetime

log_file = r"D:\GitHub_Repos\Personal_GitHub_Repos\Software-Architect-and-DevSecOps-Engineer-Road-Map\Topics\Python_Automation\Mini_Project\day_28_mp\activity_log.csv"
os.makedirs(os.path.dirname(log_file), exist_ok=True)

# Record the current time as logon
start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# If file doesn’t exist, create header
if not os.path.exists(log_file):
    with open(log_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Start_Time", "End_Time", "Duration_(minutes)"])

# Write only start time; end time will be filled later
with open(log_file, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([start_time, "", ""])

print(f"✅ Logon recorded at {start_time}")
