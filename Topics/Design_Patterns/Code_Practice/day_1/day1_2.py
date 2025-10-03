# Goal: Apply Single Responsibility Principle (SRP) in SOLID
# # ❌ SRP Violation
# class Report:
#     def __init__(self, content):
#         self.content = content

#     def print_report(self):
#         print(self.content)

#     def save_to_file(self, filename):
#         with open(filename, 'w') as f:
#             f.write(self.content)

#     def send_email(self, address):
#         print(f"Sending report to {address}...")

class Report:
    def __init__(self, content):
        self.content = content

class ReportPrinter:
    @staticmethod
    def print_report(report):
        print(report.content)

class ReportSaver:
    @staticmethod
    def save_to_file(report, filename):
        with open(filename, 'w') as f:
            f.write(report.content)

class ReportEmailer:
    @staticmethod
    def send_email(report, address):
        print(f"Sending report to {address}...")