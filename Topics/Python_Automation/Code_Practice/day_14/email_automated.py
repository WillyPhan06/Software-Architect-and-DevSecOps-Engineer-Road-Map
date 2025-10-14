import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from csv_loader import report_file, raw_file

sender_email = "timetoactcool@gmail.com"
receiver_email = "resuviketer4@gmail.com"
password = "tsjd hypb ljzp zoxi"

subject = "Daily Sales Report for Willy"
body = "Aye yo! This is automated email for sales report!"

# Create message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

# Attach the Excel file
with open(report_file, "rb") as f:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(f.read())
    print(f"Reading file {report_file}")
encoders.encode_base64(part)
print(f"Encoding file {report_file}")
part.add_header("Content-Disposition", f"attachment; filename={report_file}")
msg.attach(part)
print(f"Attached file {report_file}")

# Attach the CSV file
with open(raw_file, "rb") as f2:
    part2 = MIMEBase("application", "octet-stream")
    part2.set_payload(f2.read())
    print(f"Reading file {raw_file}")
encoders.encode_base64(part2)
print(f"Encoding file {raw_file}")
part2.add_header("Content-Disposition", f"attachment; filename={report_file}")
msg.attach(part2)
print(f"Attached file {raw_file}")

# Send email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)
    server.send_message(msg)

print("Daily report sent successfully!")
