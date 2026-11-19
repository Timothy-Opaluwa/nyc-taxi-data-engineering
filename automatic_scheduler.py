
import schedule
import time
import logging
from datetime import datetime
from pathlib import Path

# Create a folder for our log files
Path("logs").mkdir(exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def scheduled_job():
    try:
        print("\nSCHEDULED JOB STARTED", flush=True)
        logging.info("NYC Taxi scheduled job started")

        print("Execution time:", datetime.now())
        print("Simulating NYC Taxi pipeline...")

        logging.info("NYC Taxi pipeline simulation completed")
        print("SCHEDULED JOB COMPLETED!", flush=True)

    except Exception:
        logging.exception("Scheduled job failed")
        raise


schedule.every(30).seconds.do(scheduled_job)

print("NYC TAXI AUTOMATIC SCHEDULER STARTED")
print("Logging enabled: logs/pipeline.log")
print("Press Ctrl+C to stop.", flush=True)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("\nScheduler stopped by user.")
    logging.info("Scheduler stopped by user")
