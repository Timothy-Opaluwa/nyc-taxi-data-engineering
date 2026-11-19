
from pathlib import Path
import pandas as pd

# 1. Define input and output paths
raw_file = Path(
    "data/raw/yellow_tripdata_2021-01.parquet"
)

clean_folder = Path("data/processed")
clean_folder.mkdir(parents=True, exist_ok=True)

clean_file = clean_folder / "yellow_taxi_2021_01_clean.parquet"

# 2. Load raw data
print("Loading raw NYC Taxi data...")

df = pd.read_parquet(raw_file)

original_rows = len(df)

# 3. Filter pickup dates to January 2021
print("Filtering January 2021 trips...")

df_clean = df[
    (df["tpep_pickup_datetime"] >= "2021-01-01")
    &
    (df["tpep_pickup_datetime"] < "2021-02-01")
].copy()

# 4. Calculate record counts
clean_rows = len(df_clean)
removed_rows = original_rows - clean_rows

# 5. Save processed data
df_clean.to_parquet(
    clean_file,
    index=False
)

# 6. Print transformation report
print("\nTRANSFORMATION REPORT")
print("=" * 40)

print("Original records:", original_rows)
print("Cleaned records:", clean_rows)
print("Excluded records:", removed_rows)

print("\nProcessed file saved to:")
print(clean_file)

print("\nTransformation completed!")
