import pandas as pd

report_file = "daily_sales_report.xlsx"
raw_file = "sales.csv"

def main():
    df = pd.read_csv(raw_file)
    df["Revenue"] = df["Units Sold"] * df["Unit Price"]
    df = df[df["Units Sold"] > 5]
    print(df)
    df.to_excel(report_file, index=False)
    print(f"Report saved as {report_file}")

if __name__ == "__main__":
    main()
