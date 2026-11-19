
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ingest_taxi.py .
COPY validate_taxi.py .
COPY transform_taxi.py .
COPY upload_to_gcs.py .
COPY load_to_bigquery.py .
COPY check_bigquery_quality.py .
COPY run_pipeline.py .

RUN mkdir -p data/raw data/processed logs

CMD ["python", "run_pipeline.py"]
