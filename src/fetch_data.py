import os
import json
import requests
from datetime import datetime, timezone
import zipfile
import io

def fetch_datasets():
    data_dir = os.path.join("data", "raw")
    os.makedirs(data_dir, exist_ok=True)

    datasets = {
        "arms_imports": "https://api.worldbank.org/v2/en/indicator/MS.MIL.MPRT.KD?downloadformat=csv",
        "air_quality": "https://api.openaq.org/v2/measurements?country=IN&limit=1000&format=csv"
    }

    for name, url in datasets.items():
        print(f"⬇️ Downloading {name} dataset...")

        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()

            if name == "arms_imports" and url.endswith("csv"):
                file_path = os.path.join(data_dir, f"{name}.csv")
                with open(file_path, "wb") as f:
                    f.write(response.content)
            elif name == "arms_imports":
                # World Bank ZIP file
                z = zipfile.ZipFile(io.BytesIO(response.content))
                z.extractall(data_dir)
                file_path = os.path.join(data_dir, "World Bank Arms Imports Data (unzipped)")
            else:
                file_path = os.path.join(data_dir, f"{name}.csv")
                with open(file_path, "wb") as f:
                    f.write(response.content)

            meta = {
                "dataset": name,
                "source_url": url,
                "downloaded_at": datetime.now(timezone.utc).isoformat()
            }

            meta_path = os.path.join(data_dir, f"{name}_meta.json")
            with open(meta_path, "w", encoding="utf-8") as f:
                json.dump(meta, f, indent=4)

            print(f"✅ {name} saved successfully.")
            print(f"📝 Metadata saved to {meta_path}")

        except requests.exceptions.RequestException as e:
            print(f"❌ Failed to download {name}: {e}")

if __name__ == "__main__":
    fetch_datasets()

