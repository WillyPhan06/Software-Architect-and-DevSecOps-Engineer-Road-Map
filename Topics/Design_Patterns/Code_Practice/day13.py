# Overwriting the __getattr__ so when the real object extend or change methods, the proxy class can catch on that without having to implement matching methods
# virtual_proxy.py
from __future__ import annotations
from typing import Any
import time

class LargeImage:
    def __init__(self, path: str):
        print(f"[LargeImage] Loading from {path} ...")
        time.sleep(1.2)  # simulate heavy load
        self.path = path

    def show(self):
        try: 
            print(f"[LargeImage] Showing {self.path}")
            return {"status": "Succeeded"}
        except:
            return {"status": "Failed"}
        
    def rotate(self, degree: int):
        print(f"Rotating the image {degree} degree")

class ImageProxy:
    def __init__(self, path: str):
        self._path = path
        self._real: LargeImage | None = None

    def _ensure_loaded(self):
        if self._real is None:
            self._real = LargeImage(self._path)

    # preserve the same interface as LargeImage
    def show(self):
        self._ensure_loaded()
        return self._real.show()
    
    # Using __getattr__ to forward other future extended methods of the real object
    def __getattr__(self, name: str):
        self._ensure_loaded()
        return getattr(self._real, name)


# demo
if __name__ == "__main__":
    img = ImageProxy("photo.png")
    print("Proxy created quickly; image not loaded yet.")
    first_stat = img.show()   # will load on first call
    print(first_stat["status"])
    img.show()   # second call reuses the instance
    img.rotate(90)
