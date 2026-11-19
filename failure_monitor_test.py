
import logging
from pathlib import Path
from datetime import datetime

# Create logs folder if it doesn't exist
Path("logs").mkdir(exist_ok=True)

# Configure a separate failure-monitoring log
logging.basicConfig(
    filename="logs/failure_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def run_pipeline_test():
    print("STARTING PIPELINE MONITORING TEST")
    logging.info("Pipeline monitoring test started")

    try:
        print("Step 1: Extracting data...")
        logging.info("Data extraction successful")

        print("Step 2: Transforming data...")
        logging.info("Data transformation successful")

        print("Step 3: Loading data...")

        # Simulate a pipeline failure
        raise RuntimeError("Simulated BigQuery connection failure")

    except Exception:
        print("PIPELINE FAILED!")
        logging.exception("Pipeline execution failed")
        return False

    return True


if __name__ == "__main__":
    success = run_pipeline_test()

    print("Execution time:", datetime.now())

    if not success:
        print("Failure recorded in logs/failure_monitor.log")
