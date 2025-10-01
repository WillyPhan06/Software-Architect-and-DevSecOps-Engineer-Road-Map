# Simulating an Authorization Proxy with role based restrictions
# protection_proxy.py
from __future__ import annotations
from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def read(self) -> str: ...
    @abstractmethod
    def write(self, content: str) -> None: ...

class ConcreteDocument(Document):
    def __init__(self, content: str = ""):
        self._content = content

    def read(self) -> str:
        return self._content

    def write(self, content: str) -> None:
        self._content = content

class AuthProxy(Document):
    def __init__(self, doc: Document, user_roles: set[str]):
        self._doc = doc
        self._roles = user_roles

    def read(self) -> str:
        if "reader" not in self._roles and "admin" not in self._roles:
            raise PermissionError("Read denied")
        return self._doc.read()

    def write(self, content: str) -> None:
        if "writer" not in self._roles and "admin" not in self._roles:
            raise PermissionError("Write denied")
        self._doc.write(content)

# demo
if __name__ == "__main__":
    doc = ConcreteDocument("hello")
    proxy = AuthProxy(doc, {"reader"})
    print(proxy.read())            # ok
    try:
        proxy.write("new")
    except PermissionError as e:
        print("Write blocked:", e)
