
from google.cloud import bigquery

# 1. Google Cloud configuration
project_id = "stellar-polymer-513812-r1"
dataset_id = "nyc_taxi_portfolio"
table_id = "yellow_taxi_2021_01"

# 2. Source file in Google Cloud Storage
gcs_uri = (
    "gs://de-zoomcamp-practice-513812/"
    "nyc-taxi-portfolio/processed/"
    "yellow_taxi_2021_01_clean.parquet"
)

# 3. BigQuery destination
table_name = (
    f"{project_id}.{dataset_id}.{table_id}"
)

# 4. Connect to BigQuery
client = bigquery.Client(project=project_id)

# 5. Configure the load job
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.PARQUET,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
)

# 6. Load data from Cloud Storage
print("Starting BigQuery load job...")

load_job = client.load_table_from_uri(
    gcs_uri,
    table_name,
    job_config=job_config,
    location="us-central1",
)

# 7. Wait for the job to finish
load_job.result()

# 8. Verify the destination table
table = client.get_table(table_name)

print("\nBIGQUERY LOAD COMPLETED!")
print(f"Table: {table.full_table_id}")
print(f"Total rows: {table.num_rows}")
print(f"Total columns: {len(table.schema)}")
