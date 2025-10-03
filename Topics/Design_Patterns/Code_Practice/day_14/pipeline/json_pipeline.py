# pipeline/json_pipeline.py
from .base import DataPipeline
import json
from typing import Any

class JSONPipeline(DataPipeline):
    def extract(self, source: str) -> Any:
        with open(source) as fh:
            print("Ran JSON extract")
            return json.load(fh)

    def transform(self, raw):
        # pretend we filter entries
        print("Ran JSON transform")
        return [item for item in raw if item.get("active", True)]

    def load(self, data):
        print("Ran JSON load")
        return {"items": len(data)}
    
if __name__ == "__main__":
    json_pipeline = JSONPipeline()
    result = json_pipeline.run(r"D:\GitHub_Repos\Personal_Repos\Software-Architect-and-DevSecOps-Engineer-Road-Map\Topics\Design_Patterns\Code_Practice\day_14\pipeline\data.json")
    print(result)