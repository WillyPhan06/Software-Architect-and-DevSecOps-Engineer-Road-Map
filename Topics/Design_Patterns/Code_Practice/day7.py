# Added another function for third party and adapted it in the adapter class

from typing import Protocol, Any

# Client expects this interface
class StorageClient(Protocol):
    def upload(self, file_path: str) -> str:
        ...

    def write(self, file_path: str, data: bytes) -> None:
        ...

# Third-party library we can't change:
class ThirdPartyUploader:
    def send_file(self, stream: Any, meta: dict) -> dict:
        # fake implementation; in real life this streams bytes to remote
        return {"id": "remote://123", "size": len(stream)}
    
    def write_data(self, path: str, content: bytes) -> bool:
        with open(path, "wb") as f:
            f.write(content)
            print("Pre True")
            return True
        return False


# Object adapter: delegates to third-party, translates params/results
class StorageAdapter:
    def __init__(self, uploader: ThirdPartyUploader):
        self._uploader = uploader

    def upload(self, file_path: str) -> str:
        # open file as stream, translate to what third party expects
        with open(file_path, "rb") as f:
            data = f.read()
        result = self._uploader.send_file(stream=data, meta={"filename": file_path})
        return result["id"]
    
    def write(self, file_path: str, data: bytes) -> bool:
        return self._uploader.write_data(path=file_path, content=data)
if __name__ == "__main__":
    file_path = r"C:\Users\ADMIN\Downloads\example_day_7.txt"
    # Client code
    third_party = ThirdPartyUploader()
    adapter = StorageAdapter(third_party)
    
    # Now client can use the adapter as if it were a StorageClient
    file_id = adapter.upload(file_path)
    print(f"Uploaded file ID: {file_id}")

    write_stat = adapter.write(file_path, b" Handsome Willy")
    if write_stat:
        print(f"Successfully wrote data to {file_path}!")
    else:
        print(f"Failed to write data to {file_path}.")



