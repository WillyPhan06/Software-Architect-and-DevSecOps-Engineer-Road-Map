# Recoded Factory Method Pattern example for Apps on my own memory and understanding

from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod

class App(ABC):
    @abstractmethod
    def run(self, version:str) -> str:
        pass

@dataclass
class YoutubeApp(App):
    device: str
    def run(self, version: str) -> str:
        return f"Running YouTube App version {version}"
    
@dataclass
class NotionApp(App):
    device: str
    def run(self, version: str) -> str:
        return f"Running Notion App version {version}"
    
class AppFactory:
    _registry = {}

    @classmethod 
    def register_app(cls, name: str, app_class: type[App]):
        try: 
            cls._registry[name] = app_class
            print("Registered app:", name)
        except Exception as e:
            print("Error registering app:", e)

def register_all_app():
    AppFactory.register_app("youtube", YoutubeApp)
    AppFactory.register_app("notion", NotionApp)

register_all_app()