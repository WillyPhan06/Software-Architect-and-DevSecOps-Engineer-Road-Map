from openpyxl import Workbook
import random

# Create workbook and worksheet
wb = Workbook()
ws = wb.active
ws.title = "Messy Data"

# Headers
headers = ["Product", "Units Sold", "Unit Price", "Revenue", "Notes", "Extra"]
ws.append(headers)

# Some random messy data
products = ["  Apple", "Banana  ", "Orange", "Mango", "", None, "Peach!", "Grapes@", "Pineapple", "Kiwi"]
notes = ["Good", " ", None, "Check#", "??", "N/A", "", "Urgent!", "Sold Out", None]

for i in range(10):
    row = [
        random.choice(products),                        # messy product name
        random.choice([5, "10", None, "seven", 0]),    # units sold (mixed types)
        random.choice([1.5, "2.5", None, "three"]),    # unit price (mixed types)
        random.choice([10, None, "20", "thirty"]),     # revenue (mixed types)
        random.choice(notes),                           # notes messy
        random.choice([None, "Extra", 999, "", "???"]) # extra random column
    ]
    ws.append(row)

# Save file
wb.save("super_messy_data.xlsx")
print("Super messy Excel file generated!")
