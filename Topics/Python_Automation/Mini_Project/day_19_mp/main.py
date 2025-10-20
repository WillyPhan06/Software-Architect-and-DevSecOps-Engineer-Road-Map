import requests
import json
import pandas as pd

class Main:
    def fetch_json_from_url(self, url):
        return requests.get(url).json()

    def fetch_json_from_url_flow(self):
        while True:
            url = input("Please enter the URL to fetch JSON from (q to go back): ")
            if url.lower() == 'q':
                return
            try:
                data = self.fetch_json_from_url(url)
                print("Fetched JSON data:")
                print(json.dumps(data, indent=4))
            except Exception as e:
                print(f"An error occurred: {e}")

    def create_csv_xlsx_from_url(self):
        while True:
            url = input("Please enter the URL to create CSV/XLSX from (q to go back): ")
            file_name = input("Please enter the desired file name: ")
            if url.lower() == 'q':
                return
            try:
                data = self.fetch_json_from_url(url)
                df = pd.DataFrame(data)
                df.to_csv(f"{file_name}.csv", index=False)
                print(f"CSV file: {file_name}.csv created successfully.")
                df.to_excel(f"{file_name}.xlsx", index=False)
                print(f"XLSX file: {file_name}.xlsx created successfully.")

            except Exception as e:
                print(f"An error occurred: {e}")
                continue
            


    def main_menu(self):
        while True:
            print("--- Welcome to the Main Menu ---")
            print("1. Fetch JSON from URL")
            print("2. Create CSV/XLSX from URL")
            print("q. Exit")
            choice = input("Please enter your choice (1-2): ")
            if choice == '1':
                self.fetch_json_from_url_flow()
            elif choice == '2':
                self.create_csv_xlsx_from_url()
            elif choice.lower() == 'q':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_app = Main()
    main_app.main_menu()
