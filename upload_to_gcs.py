
from pathlib import Path
from google.cloud import storage

# 1. Google Cloud configuration
project_id = "stellar-polymer-513812-r1"
bucket_name = "de-zoomcamp-practice-513812"

# 2. Local processed dataset
local_file = Path(
    "data/processed/yellow_taxi_2021_01_clean.parquet"
)

# 3. Destination in Google Cloud Storage
destination_blob = (
    "nyc-taxi-portfolio/"
    "processed/yellow_taxi_2021_01_clean.parquet"
)

# 4. Check the local file exists
if not local_file.is_file():
    raise FileNotFoundError(
        f"Processed dataset not found: {local_file}"
    )

# Validate the processed Parquet file before uploading

import pandas as pd

print("Checking processed dataset before upload...")

df = pd.read_parquet(local_file)

expected_rows = 1369745

if len(df) != expected_rows:
    raise ValueError(
        f"Unexpected row count: {len(df)}. "
        f"Expected: {expected_rows}"
    )

if df.empty:
    raise ValueError("Processed dataset is empty!")

print("Processed dataset validation: PASS")
print(f"Verified records: {len(df)}")

del df

# 5. Authenticate using Application Default Credentials
print("Connecting to Google Cloud Storage...")

client = storage.Client(project=project_id)

# 6. Access the bucket and create an object reference
bucket = client.bucket(bucket_name)
blob = bucket.blob(destination_blob)

# 7. Upload the Parquet file
print("Uploading NYC Taxi dataset...")

blob.upload_from_filename(
    str(local_file),
    content_type="application/octet-stream"
)

# 8. Confirm upload
print("\nUPLOAD COMPLETED SUCCESSFULLY!")
print(f"Bucket: {bucket_name}")
print(f"File: {destination_blob}")
print(f"Cloud path: gs://{bucket_name}/{destination_blob}")
