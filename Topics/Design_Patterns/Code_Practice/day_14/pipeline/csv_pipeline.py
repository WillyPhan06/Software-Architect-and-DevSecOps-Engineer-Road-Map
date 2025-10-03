# pipeline/csv_pipeline.py
from __future__ import annotations
import csv
from typing import List, Dict, Any
# import os
# import sys

# # Ensure pipeline can be imported when running as a script
# if __name__ == "__main__" and __package__ is None:
#     # Add parent directory to sys.path
#     parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     sys.path.insert(0, parent_dir)
#     __package__ = "pipeline"

from .base import DataPipeline

class CSVPipeline(DataPipeline):
    def extract(self, source: str) -> List[Dict[str, str]]:
        with open(source, newline='') as fh:
            reader = csv.DictReader(fh)
            return list(reader)

    def transform(self, raw):
        return [{k.strip().lower(): v.strip() for k, v in row.items()} for row in raw]

    def validate(self, data):
        if not data:
            raise ValueError("No rows found")
        if "id" not in data[0]:
            raise ValueError("Missing 'id' column")

    def load(self, data):
        return {"rows": len(data)}

# Only runs when this file is executed directly
if __name__ == "__main__":
    csv_path = r"D:\GitHub_Repos\Personal_Repos\Software-Architect-and-DevSecOps-Engineer-Road-Map\Topics\Design_Patterns\Code_Practice\day_14\pipeline\data.csv"
    csv_pipeline = CSVPipeline()
    result = csv_pipeline.run(csv_path)
    print(result)
