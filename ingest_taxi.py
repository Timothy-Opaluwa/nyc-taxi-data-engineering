
from pathlib import Path
import requests
import pandas as pd

# 1. Define the dataset URL
url = (
    "https://d37ci6vzurychx.cloudfront.net/"
    "trip-data/yellow_tripdata_2021-01.parquet"
)

# 2. Create a folder for raw data
data_folder = Path("data/raw")
data_folder.mkdir(parents=True, exist_ok=True)

# 3. Define where to save the file
file_path = data_folder / "yellow_tripdata_2021-01.parquet"

# 4. Download the dataset
print("Downloading NYC Yellow Taxi data...")

with requests.get(url, stream=True, timeout=60) as response:
    response.raise_for_status()

    with open(file_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                file.write(chunk)

print("Download completed!")

# 5. Read the Parquet file
df = pd.read_parquet(file_path)

# 6. Inspect the dataset
print("\nFirst five rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nTotal records:")
print(len(df))
