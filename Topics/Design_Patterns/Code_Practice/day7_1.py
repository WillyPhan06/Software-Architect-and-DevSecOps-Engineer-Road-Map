# An example of class Adapter (less common in Python) because it's too messy compared to object adapter which you can just wrap the object

class LegacyStorage:
    # Old interface
    def put(self, path: str, content: bytes) -> str:
        return f"legacy://{path}"

class ClassAdapter(LegacyStorage):
    # Adapt to new interface expected by client
    def upload(self, file_path: str) -> str:
        with open(file_path, "rb") as f:
            content = f.read()
        return self.put(file_path, content)

# Usage:
# storage = ClassAdapter()
# storage.upload("test.txt")
