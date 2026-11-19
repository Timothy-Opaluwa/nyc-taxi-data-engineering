
import pandas as pd
from pathlib import Path

# 1. Locate our downloaded dataset
file_path = Path(
    "data/raw/yellow_tripdata_2021-01.parquet"
)

# 2. Read the dataset
df = pd.read_parquet(file_path)

print("NYC TAXI DATA QUALITY REPORT")
print("=" * 40)

# 3. Check dataset dimensions
print("\nTotal rows:", len(df))
print("Total columns:", len(df.columns))

# 4. Check missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# 5. Check negative fare amounts
negative_fares = (df["fare_amount"] < 0).sum()

print("\nTrips with negative fares:")
print(negative_fares)

# 6. Check negative trip distances
negative_distances = (
    df["trip_distance"] < 0
).sum()

print("\nTrips with negative distances:")
print(negative_distances)

# 7. Check pickup date range
print("\nEarliest pickup:")
print(df["tpep_pickup_datetime"].min())

print("\nLatest pickup:")
print(df["tpep_pickup_datetime"].max())

# 8. Check records outside January 2021
outside_january = (
    (df["tpep_pickup_datetime"] < "2021-01-01")
    |
    (df["tpep_pickup_datetime"] >= "2021-02-01")
).sum()

print("\nTrips outside January 2021:")
print(outside_january)

print("\nValidation report completed!")

# 9. Apply mandatory data quality checks

print("\nRUNNING MANDATORY QUALITY CHECKS")
print("=" * 40)

required_columns = [
    "tpep_pickup_datetime",
    "trip_distance",
    "fare_amount",
    "passenger_count",
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

checks = {
    "Dataset is not empty": len(df) > 0,
    "No required columns missing": len(missing_columns) == 0,
    "No missing pickup timestamps":
        df["tpep_pickup_datetime"].notna().all(),
    "No negative trip distances":
        negative_distances == 0,
}

for check_name, passed in checks.items():
    status = "PASS" if passed else "FAIL"
    print(f"{check_name}: {status}")

if not all(checks.values()):
    raise RuntimeError(
        "Raw data quality checks failed. Pipeline stopped."
    )

print("\nRAW DATA QUALITY GATE PASSED!")
