#MVP of OOP design of a script that currently have 1 functionality of reading JSON file

from dataclasses import dataclass, field
from typing import Dict, List, Set, Type
from abc import ABC, abstractmethod
import json
import csv
import sys

@dataclass
class JSON_Files:
    files: Set[str] = field(default_factory=set)


@dataclass
class CSV_Files:
    files: Set[str] = field(default_factory=set)


class JSON_Files_Interaction:
    pass

class CSV_Files_Interaction:
    pass

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
    main = Main()
    main.run()



