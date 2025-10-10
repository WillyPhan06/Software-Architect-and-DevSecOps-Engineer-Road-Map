import PyPDF2
from abc import ABC, abstractmethod

class Menu(ABC):
    @abstractmethod
    def display_description(self):
        pass

    @abstractmethod
    def run(self):
        pass

class CountWordsMenu(Menu):
    def display_description(self):
        return "Count the number of words in a PDF document."
    
    def run(self):
        file_path = input("Enter the path to the PDF file: ")
        try:
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                total_words = 0
                for page in reader.pages:
                    text = page.extract_text()
                    total_words += len(text.split())
                print(f"Total number of words: {total_words}")
        except Exception as e:
            print(f"An error occurred: {e}")

class CountUniqueWordsMenu(Menu):
    def display_description(self):
        return "Count the number of unique words in a PDF document."
    
    def run(self):
        file_path = input("Enter the path to the PDF file: ")
        try:
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                unique_words = set()
                for page in reader.pages:
                    text = page.extract_text()
                    words = text.split()
                    unique_words.update(words)
                print(f"Total number of unique words: {len(unique_words)}")
        except Exception as e:
            print(f"An error occurred: {e}")

class CountWordsFrequencyMenu(Menu):
    def display_description(self):
        return "Count the frequency of each word in a PDF document."
    
    def run(self):
        from collections import Counter
        file_path = input("Enter the path to the PDF file: ")
        try:
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                word_counter = Counter()
                for page in reader.pages:
                    text = page.extract_text()
                    words = text.split()
                    word_counter.update(words)
                for word, count in word_counter.most_common():
                    print(f"{word}: {count}")
        except Exception as e:
            print(f"An error occurred: {e}")

class SaveToTextFileMenu(Menu):
    def display_description(self):
        return "Save the text content of a PDF document to a text file."
    
    def run(self):
        file_path = input("Enter the path to the PDF file: ")
        output_path = input("Enter the path for the output text file: ")
        try:
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                with open(output_path, 'w', encoding='utf-8') as output_file:
                    for page in reader.pages:
                        text = page.extract_text()
                        output_file.write(text + "\n")
            print(f"Text content saved to {output_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

class MenuAutoRegistry:
    menu_instances = [cls() for cls in Menu.__subclasses__()]


class Main:
    def run():
        while True:
            print("\nMenu Options:")
            for idx, menu in enumerate(MenuAutoRegistry.menu_instances, start=1):
                print(f"{idx}. {menu.display_description()}")
            print("0. Exit")
            
            choice = input("Select an option: ")
            if choice == '0':
                print("Exiting the program.")
                break
            
            try:
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(MenuAutoRegistry.menu_instances):
                    MenuAutoRegistry.menu_instances[choice_idx].run()
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    Main.run()