
from datetime import datetime

def scheduled_job():
    print("SCHEDULED JOB STARTED")
    print("Execution time:", datetime.now())
    print("Simulating NYC Taxi pipeline execution...")
    print("SCHEDULED JOB COMPLETED SUCCESSFULLY!")

if __name__ == "__main__":
    scheduled_job()
