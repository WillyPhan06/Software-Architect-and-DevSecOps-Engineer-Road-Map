# TODO: implement file_manager.py
import os
import shutil

class FileManager:
    def __init__(self, root_folder):
        self.root = os.path.abspath(root_folder)
        self.pdf_folder = os.path.join(self.root, "pdfs")
        self.txt_folder = os.path.join(self.root, "txts")
        self.uncategorized_folder = os.path.join(self.root, "uncategorized")
        self.ensure_folders()

    def ensure_folders(self):
        for folder in [self.pdf_folder, self.txt_folder, self.uncategorized_folder]:
            os.makedirs(folder, exist_ok=True)

    def resolve_path(self, input_path_or_name, expected_type):
        """
        Returns absolute path of file. If only name is given, search in corresponding folder.
        expected_type: "pdf" or "txt"
        """
        if os.path.isabs(input_path_or_name) and os.path.isfile(input_path_or_name):
            return os.path.abspath(input_path_or_name)

        # Search in the folder
        folder = self.pdf_folder if expected_type == "pdf" else self.txt_folder
        candidate = os.path.join(folder, input_path_or_name)
        if os.path.isfile(candidate):
            return candidate

        raise FileNotFoundError(f"File '{input_path_or_name}' not found in '{folder}' or as absolute path.")

    def categorize_file(self, file_path):
        """
        Moves file to correct folder if misplaced, or uncategorized if unknown type.
        Returns new path of the file.
        """
        ext = os.path.splitext(file_path)[1].lower()
        file_name = os.path.basename(file_path)

        # Determine target folder
        if ext == ".pdf":
            target_folder = self.pdf_folder
        elif ext == ".txt":
            target_folder = self.txt_folder
        else:
            target_folder = self.uncategorized_folder

        # Check if already in correct folder
        if os.path.abspath(os.path.dirname(file_path)) == os.path.abspath(target_folder):
            return file_path

        # Move file
        target_path = os.path.join(target_folder, file_name)
        shutil.move(file_path, target_path)
        return target_path
