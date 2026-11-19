
import sys
import logging
from pathlib import Path

Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    filename="logs/exit_code_test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def run_test():
    try:
        print("Starting pipeline test...")
        logging.info("Pipeline test started")

        print("Extracting data...")
        print("Transforming data...")
        print("Loading data...")

        # Deliberately simulate a failure
        raise RuntimeError("Simulated database connection failure")

    except Exception:
        logging.exception("Pipeline failed")
        print("PIPELINE FAILED!")
        return 1

    return 0


if __name__ == "__main__":
    exit_code = run_test()
    sys.exit(exit_code)
