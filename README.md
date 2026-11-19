# NYC Taxi Data Engineering Pipeline

An end-to-end Data Engineering portfolio project using Python, Docker, Google Cloud Storage, and Google BigQuery.

## Project Overview

This project implements an automated ETL (Extract, Transform, Load) pipeline to process New York City Yellow Taxi trip records for January 2021.

The pipeline downloads raw trip data, validates data quality, transforms the dataset, uploads the processed data to Google Cloud Storage, loads it into BigQuery, and performs automated quality checks.

## Technologies Used

- **Python:** Data ingestion, validation, transformation, and orchestration
- **Pandas:** Data processing and transformation
- **PyArrow:** Parquet file handling
- **Docker:** Containerization and reproducible execution
- **Google Cloud Storage:** Cloud-based data storage
- **Google BigQuery:** Data warehousing and analytical queries
- **Git and GitHub:** Version control and project documentation
- **Python logging:** Pipeline execution history and failure monitoring

## Pipeline Architecture

```text
NYC Yellow Taxi Parquet Dataset
              |
              v
       Python Ingestion
              |
              v
       Data Validation
              |
              v
      Data Transformation
              |
              v
     Google Cloud Storage
              |
              v
        Google BigQuery
              |
              v
      Data Quality Checks
```

## Dataset

Source: NYC Taxi and Limousine Commission (TLC) Yellow Taxi Trip Records, January 2021.

| Metric | Value |
|---|---|
| Raw records | 1,369,769 |
| Records excluded | 24 |
| Processed records | 1,369,745 |
| Dataset columns | 19 |
| File format | Parquet |

The transformation retains trips with pickup timestamps within January 2021.

## Data Quality Checks

The pipeline validates:

- Required columns and nonempty datasets
- Missing pickup timestamps
- Negative trip distances
- Expected record counts
- Pickup timestamps within January 2021

Additional observations include missing passenger counts and negative fare amounts. These are reported but do not currently cause the pipeline to fail.

## Project Structure

```text
nyc-taxi-data-engineering/
├── ingest_taxi.py
├── validate_taxi.py
├── transform_taxi.py
├── upload_to_gcs.py
├── load_to_bigquery.py
├── check_bigquery_quality.py
├── run_pipeline.py
├── create_bigquery_dataset.py
├── automatic_scheduler.py
├── scheduler_test.py
├── failure_monitor_test.py
├── exit_code_test.py
├── test_pipeline.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```


## Pipeline Execution

The main pipeline orchestrator is `run_pipeline.py`.

### Install Dependencies

To install the required Python packages, run:

```bash
python -m pip install -r requirements.txt
```

### Run the Pipeline

After configuring Google Cloud credentials, execute:

```bash
python run_pipeline.py
```

### Build the Docker Image

To build the Docker image, run:

```bash
docker build -t nyc-taxi-pipeline:3.0 .
```

### Google Cloud Configuration

Running the full pipeline requires Google Cloud Application Default Credentials with appropriate permissions and access to the configured project resources.

**Important:** The current pipeline uses a fixed January 2021 dataset and overwrites its existing processed Cloud Storage object and BigQuery destination table on each successful load.


## Scheduling and Monitoring

The project also includes educational exercises demonstrating:

- Recurring job scheduling using Python's `schedule` library
- Execution logging
- Failure simulation and exception handling
- Process exit codes
- Persistent Docker logs using bind mounts

The scheduling exercises are simulations and are not yet connected to production cloud orchestration.

## Results

The pipeline successfully processed **1,369,745 January 2021 taxi records** and loaded them into Google BigQuery.

The complete six-stage workflow was executed successfully inside Docker, with an observed execution time of **22.53 seconds** in one test run.

## Future Improvements

- Parameterize dataset months and cloud destinations
- Introduce incremental processing
- Add automated unit and integration tests
- Implement cloud-based scheduling
- Add monitoring and alerting
- Build analytical SQL queries and dashboards

## Project Purpose

This project demonstrates practical Data Engineering skills, including ETL development, cloud storage integration, data warehousing, containerization, data quality validation, pipeline orchestration, and error monitoring.