#MVP of OOP design of a script that currently have 1 functionality of reading JSON file
from typing import List, Type
from abc import ABC
import json
import csv
import sys

class Menu(ABC):
    pass

class Read_Json_Menu(Menu):
    @staticmethod
    def get_menu_desc():
        return "Read from JSON files"
    

    @staticmethod
    def run():
        while True:
            print("--- READ FROM JSON FILES MENU ---")
            json_file = input("Please enter the full location of json_file you want to read (q to quit): ")
            if json_file.lower() == "q":
                print("Quitting Read Json Menu...")
                return
            elif json_file[-5:] != ".json":
                print("Invalid file type! Must end with .json!")
                continue
            else:
                try:
                    with open(json_file, "r") as jsf:
                        data = json.load(jsf)
                        print(f"Successfully read from {json_file}")
                        print("Result:")
                        print(data)
                        continue
                except Exception as e:
                    print(f"Error occured while trying to read JSON file: {e}")
                    continue
                
class Read_CSV_Menu(Menu):
    @staticmethod
    def get_menu_desc():
        return "Read from CSV files"
    
    @staticmethod
    def run():
        while True:
            print("--- READ FROM CSV FILES MENU ---")
            csv_file = input("Please enter the full location of csv_file you want to read (q to quit): ")
            if csv_file.lower() == "q":
                print("Quitting Read CSV Menu...")
                return
            elif csv_file[-4:] != ".csv":
                print("Invalid file type! Must end with .csv!")
                continue
            else:
                try:
                    with open(csv_file, "r") as csvf:
                        reader = csv.DictReader(csvf)
                        print(f"Successfully read from {csv_file}")
                        print("Result: ")
                        for row in reader:
                            print(row)
                        continue
                except Exception as e:
                    print(f"Error occured while trying to read CSV file: {e}")
                    continue

class Write_JSON_Menu(Menu):
    @staticmethod
    def get_menu_desc():
        return "Write to JSON files"

    @staticmethod
    def run():
        while True:
            print("--- WRITE TO JSON FILES MENU ---")
            json_file = input("Enter full path of JSON file to write (q to quit): ")
            if json_file.lower() == "q":
                print("Quitting Write JSON Menu...")
                return
            elif not json_file.endswith(".json"):
                print("Invalid file type! Must end with .json!")
                continue
            else:
                try:
                    # Get Python dict from user input
                    user_input = input("Enter a Python dict or list (e.g., {'key': 'value'}): ")
                    data = eval(user_input)  # ⚠️ unsafe for production, ok for uni practice
                    with open(json_file, "w") as f:
                        json.dump(data, f, indent=4)
                    print(f"Successfully wrote to {json_file}")
                    print("Result:")
                    print(data)
                except Exception as e:
                    print(f"Error while writing JSON: {e}")


class Write_CSV_Menu(Menu):
    @staticmethod
    def get_menu_desc():
        return "Write to CSV files"

    @staticmethod
    def run():
        while True:
            print("--- WRITE TO CSV FILES MENU ---")
            csv_file = input("Enter full path of CSV file to write (q to quit): ")
            if csv_file.lower() == "q":
                print("Quitting Write CSV Menu...")
                return
            elif not csv_file.endswith(".csv"):
                print("Invalid file type! Must end with .csv!")
                continue
            else:
                try:
                    # Ask for headers
                    headers_input = input("Enter comma-separated headers (e.g., name,age): ")
                    headers = [h.strip() for h in headers_input.split(",")]

                    rows = []
                    while True:
                        row_input = input("Enter comma-separated values for a row (or 'q' to quit): ")
                        if row_input.lower() == "q":
                            break
                        values = [v.strip() for v in row_input.split(",")]
                        if len(values) != len(headers):
                            print("Number of values does not match number of headers!")
                            continue
                        rows.append(dict(zip(headers, values)))

                    with open(csv_file, "w", newline="") as f:
                        writer = csv.DictWriter(f, fieldnames=headers)
                        writer.writeheader()
                        writer.writerows(rows)

                    print(f"Successfully wrote to {csv_file}")
                    print("Result:")
                    for r in rows:
                        print(r)

                except Exception as e:
                    print(f"Error while writing CSV: {e}")


class Menu_Registration:
    registry: List[Type[Menu]] = []

    @classmethod
    def register(cls, menu: Type[Menu]):
        cls.registry.append(menu)

    @staticmethod
    def get_menu_desc(menu: Type[Menu]):
        description = menu.get_menu_desc()
        return description
        


class Main:
    def run(self):
        while True:
            menu_len = len(Menu_Registration.registry)
            print("--- MAIN MENU ---")
            for i in range(menu_len):
                print(f"{i+1}. {Menu_Registration.get_menu_desc(menu=Menu_Registration.registry[i])}")
            choice = input("Choose an option based on number (q to quit): ").lower()
            if choice == "q":
                print("Quitting the program! See you again!")
                sys.exit()
            elif choice.isdigit() and int(choice) <= menu_len:
                Menu_Registration.registry[int(choice)-1].run()
                continue
            else:
                print("Invalid choice! Choose a number again!")
                continue







if __name__ == "__main__":
    Menu_Registration.register(Read_Json_Menu)
    Menu_Registration.register(Read_CSV_Menu)
    Menu_Registration.register(Write_JSON_Menu)
    Menu_Registration.register(Write_CSV_Menu)
    main = Main()
    main.run()



