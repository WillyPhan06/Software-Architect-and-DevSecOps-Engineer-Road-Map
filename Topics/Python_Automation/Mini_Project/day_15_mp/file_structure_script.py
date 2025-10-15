import os

# Root folder for the project
root = "pdf_txt_converter_project"

# Folder structure
folders = [
    "commands",
    "converters",
    "utils",
    "settings"
]

# Files to create inside each folder
files = {
    "": ["main.py"],  # root files
    "commands": ["__init__.py", "base.py", "pdf_to_txt.py", "txt_to_pdf.py", "settings.py"],
    "converters": ["__init__.py", "base.py", "pdf_to_txt.py", "txt_to_pdf.py"],
    "utils": ["__init__.py", "file_manager.py", "email_sender.py"],
    "settings": ["__init__.py", "settings_manager.py"]
}

# Create root folder
os.makedirs(root, exist_ok=True)

# Create subfolders and files
for folder in folders:
    folder_path = os.path.join(root, folder)
    os.makedirs(folder_path, exist_ok=True)

# Create all files
for folder, file_list in files.items():
    for file_name in file_list:
        file_path = os.path.join(root, folder, file_name) if folder else os.path.join(root, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            # For base files, put minimal class/interface template
            if file_name == "base.py" and folder in ["commands", "converters"]:
                if folder == "commands":
                    f.write("from abc import ABC, abstractmethod\n\n")
                    f.write("class Command(ABC):\n")
                    f.write("    @abstractmethod\n")
                    f.write("    def execute(self):\n")
                    f.write("        pass\n")
                else:
                    f.write("from abc import ABC, abstractmethod\n\n")
                    f.write("class Converter(ABC):\n")
                    f.write("    @abstractmethod\n")
                    f.write("    def convert(self, input_path: str, output_path: str):\n")
                    f.write("        pass\n")
            else:
                f.write("# TODO: implement " + file_name + "\n")

print(f"Project structure created successfully in '{root}' folder.")
