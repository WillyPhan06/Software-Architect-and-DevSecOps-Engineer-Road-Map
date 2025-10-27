import os
import pandas as pd

def save_to_csv(data: list[dict], filename: str = "laptops_data.csv", append: bool = False):
    """Save scraped data to CSV in /data/output/."""
    os.makedirs("data/output", exist_ok=True)
    path = os.path.join("data/output", filename)

    df = pd.DataFrame(data)

    if append and os.path.exists(path):
        df.to_csv(path, mode="a", header=False, index=False, encoding="utf-8-sig")
        print(f"📎 Appended {len(df)} rows to {path}")
    else:
        df.to_csv(path, index=False, encoding="utf-8-sig")
        print(f"✅ Saved {len(df)} rows to {path}")
