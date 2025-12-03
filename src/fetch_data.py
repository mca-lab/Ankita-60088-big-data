import os
import requests
import pandas as pd

RAW_DATA_DIR = "data/raw"
os.makedirs(RAW_DATA_DIR, exist_ok=True)

DATASETS = {
    "population": "https://raw.githubusercontent.com/datasets/population/master/data/population.csv",
    "co2_emissions": "https://raw.githubusercontent.com/datasets/co2-fossil-global/master/global.csv"
}

def fetch_and_store(name, url):
    print(f"Downloading {name} dataset...")
    
    response = requests.get(url)
    response.raise_for_status()
    
    csv_path = os.path.join(RAW_DATA_DIR, f"{name}.csv")
    
    with open(csv_path, "wb") as f:
        f.write(response.content)

    print(f"Saved CSV: {csv_path}")

    # Optional: Convert to Parquet
    df = pd.read_csv(csv_path)
    parquet_path = os.path.join(RAW_DATA_DIR, f"{name}.parquet")
    df.to_parquet(parquet_path, index=False)

    print(f"Saved Parquet: {parquet_path}\n")

def main():
    for name, url in DATASETS.items():
        fetch_and_store(name, url)

    print("✅ All datasets downloaded and stored successfully.")

if __name__ == "__main__":
    main()
