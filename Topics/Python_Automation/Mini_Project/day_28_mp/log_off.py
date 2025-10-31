import csv
import os
from datetime import datetime

log_file = r"D:\GitHub_Repos\Personal_GitHub_Repos\Software-Architect-and-DevSecOps-Engineer-Road-Map\Topics\Python_Automation\Mini_Project\day_28_mp\activity_log.csv"
if not os.path.exists(log_file):
    exit()

end_time = datetime.now()
end_str = end_time.strftime("%Y-%m-%d %H:%M:%S")

# Read the last non-empty line
with open(log_file, "r+", newline="", encoding="utf-8") as f:
    lines = f.readlines()
    if len(lines) <= 1:
        exit()  # no sessions yet

    last_line = lines[-1].strip().split(",")
    if last_line[1] == "":
        start = datetime.strptime(last_line[0], "%Y-%m-%d %H:%M:%S")
        duration = round((end_time - start).total_seconds() / 60, 2)
        last_line[1] = end_str
        last_line[2] = str(duration)

        # Replace the last line and rewrite just that part
        lines[-1] = ",".join(last_line) + "\n"
        f.seek(0)
        f.writelines(lines)

print(f"🛑 Logoff recorded at {end_str}")
