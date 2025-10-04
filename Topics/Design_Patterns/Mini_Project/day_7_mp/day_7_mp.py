# Writing a file writing program using adapter pattern with decorator, the cons in here is the client class link back to the adapter class which is not a good practice making it tightly coupled

from __future__ import annotations
from dataclasses import dataclass
from functools import wraps

# Decorator for extending functionality of adapter method "write"
def adapter_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Adapter decorator: Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Adapter decorator: Finished {func.__name__}")
        return result
    return wrapper

class LegacyFileWriter:
    def write_data(self, path: str, content: bytes) -> bool:
        with open(path, "wb") as f:
            f.write(content)
            return True
        return False
    
@dataclass
class NewFileWriter:
    file_writer_adapter: FileWriterAdapter
    def write(self, path: str, content: bytes) -> bool:
        return self.file_writer_adapter.write(path, content)

@dataclass
class FileWriterAdapter:
    legacy_file_writer: LegacyFileWriter

    @adapter_decorator
    def write(self, path: str, content: bytes) -> bool:
        return self.legacy_file_writer.write_data(path, content)
    
if __name__ == "__main__":
    legacy_writer = LegacyFileWriter()
    file_writer_adapter = FileWriterAdapter(legacy_writer)
    new_file_writer = NewFileWriter(file_writer_adapter)
    file_path = r"C:\Users\ADMIN\Downloads\example_day_7.txt"
    write_stat = new_file_writer.write(file_path, b" Hello Friendzy")
    if write_stat:
        print(f"Successfully wrote data to {file_path}!")
    else:
        print(f"Failed to write data to {file_path}.")

    




