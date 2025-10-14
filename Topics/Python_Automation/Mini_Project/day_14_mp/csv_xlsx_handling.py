from dataclasses import dataclass
import pandas as pd


@dataclass
class CSV_XLSX_Handler:
    csv_path: str
    xlsx_path: str

    def convert_csv_to_xlsx(self):
        df = pd.read_csv(self.csv_path)
        df.to_excel(self.xlsx_path, index=False)
