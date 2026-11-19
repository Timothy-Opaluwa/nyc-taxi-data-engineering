
from google.cloud import bigquery

# Google Cloud configuration
project_id = "stellar-polymer-513812-r1"
dataset_id = "nyc_taxi_portfolio"

# Connect to BigQuery
client = bigquery.Client(project=project_id)

# Define the full dataset name
dataset_name = f"{project_id}.{dataset_id}"

# Configure the dataset
dataset = bigquery.Dataset(dataset_name)
dataset.location = "us-central1"

print("Creating BigQuery dataset...")

# Create the dataset only if it does not exist
dataset = client.create_dataset(
    dataset,
    exists_ok=True
)

print("\nBIGQUERY DATASET READY!")
print(f"Dataset: {dataset.full_dataset_id}")
print(f"Location: {dataset.location}")
