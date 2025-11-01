import subprocess
import os
import time
from fpdf import FPDF

LOG_FILE = "process.log"
PDF_FILE = "sample.pdf"

def last_log_line():
    if not os.path.exists(LOG_FILE):
        return ""
    with open(LOG_FILE, "r") as f:
        lines = f.readlines()
        for line in reversed(lines):
            if line.strip():
                return line.strip() or ""

def fix_problem(log_line):
    """Tries to automatically fix common issues."""
    error_keywords = {"FileNotFoundError", "not found"} 
    if any(keyword in log_line for keyword in error_keywords):
        print("[Fix] PDF file missing. Creating a dummy sample.pdf...")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="This is a real PDF.", ln=True)
        pdf.output("sample.pdf")
        return True
    return False

def rerun_script():
    print("[Action] Rerunning pdf_reader.py...")
    subprocess.run(["python", "pdf_reader.py"])

def main():
    print("[Monitor] Checking process.log for issues...")
    line = last_log_line()
    if not line:
        print("[Info] No logs found yet.")
        return

    if "ERROR" in line:
        print(f"[Detected Error] {line}")
        if fix_problem(line):
            time.sleep(1)
            rerun_script()
        else:
            print("[Fix] No known fix for this error.")
    else:
        print("[OK] No errors found in the log.")

if __name__ == "__main__":
    main()
