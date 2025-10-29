# daily_report.py
from datetime import datetime

with open("daily_log.txt", "a") as f:
    f.write(f"User Logged in ran at {datetime.now()}\n")
print("✅ Daily report generated!")
