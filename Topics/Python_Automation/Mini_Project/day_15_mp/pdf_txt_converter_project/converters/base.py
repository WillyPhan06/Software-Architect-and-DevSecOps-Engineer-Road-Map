from abc import ABC, abstractmethod

class Converter(ABC):
    @abstractmethod
    def convert(self, input_path: str, output_path: str):
        pass
