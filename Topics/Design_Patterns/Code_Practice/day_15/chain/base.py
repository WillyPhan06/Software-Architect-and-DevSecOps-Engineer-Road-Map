# chain/base.py
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

class Handler(ABC):
    def __init__(self, successor: Optional[Handler] = None):
        self._successor = successor

    def set_successor(self, successor: Handler):
        self._successor = successor

    def handle(self, request: dict):
        if self._can_handle(request):
            return self._process(request)
        elif self._successor:
            return self._successor.handle(request)
        else:
            return self._unhandled(request)

    @abstractmethod
    def _can_handle(self, request: dict) -> bool:
        ...

    @abstractmethod
    def _process(self, request: dict):
        ...

    def _unhandled(self, request: dict):
        print(f"No handler could process request: {request}")
