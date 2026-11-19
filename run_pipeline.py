
import subprocess
import sys
import time
import logging
from pathlib import Path

# Create a directory for log files
Path("logs").mkdir(exist_ok=True)

# Configure pipeline logging
logging.basicConfig(
    filename="logs/nyc_taxi_pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

PIPELINE_STEPS = [
    "ingest_taxi.py",
    "validate_taxi.py",
    "transform_taxi.py",
    "upload_to_gcs.py",
    "load_to_bigquery.py",
    "check_bigquery_quality.py",
]


def run_pipeline():
    print("STARTING NYC TAXI DATA PIPELINE", flush=True)
    logging.info("NYC Taxi pipeline started")

    start_time = time.time()

    for step in PIPELINE_STEPS:
        print(f"\nRunning: {step}", flush=True)
        logging.info("Starting step: %s", step)

        try:
            subprocess.run(
                [sys.executable, step],
                check=True
            )

            print(f"COMPLETED: {step}", flush=True)
            logging.info("Completed step: %s", step)

        except subprocess.CalledProcessError:
            print(f"PIPELINE FAILED at {step}", flush=True)
            logging.exception("Pipeline failed at step: %s", step)
            return 1

    duration = round(time.time() - start_time, 2)

    print("\nALL PIPELINE STEPS COMPLETED SUCCESSFULLY!")
    print(f"Total execution time: {duration} seconds")

    logging.info(
        "Pipeline completed successfully in %s seconds",
        duration
    )

    return 0


if __name__ == "__main__":
    sys.exit(run_pipeline())
