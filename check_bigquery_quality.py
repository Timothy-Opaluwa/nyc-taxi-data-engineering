
from google.cloud import bigquery

PROJECT_ID = "stellar-polymer-513812-r1"
TABLE_ID = (
    f"{PROJECT_ID}.nyc_taxi_portfolio.yellow_taxi_2021_01"
)

EXPECTED_ROWS = 1369745

client = bigquery.Client(project=PROJECT_ID)

query = f"""
SELECT
    COUNT(*) AS total_records,
    COUNTIF(
        DATE(tpep_pickup_datetime)
        NOT BETWEEN '2021-01-01' AND '2021-01-31'
    ) AS invalid_dates,
    COUNTIF(trip_distance < 0) AS negative_distances,
    COUNTIF(passenger_count IS NULL) AS missing_passengers,
    COUNTIF(fare_amount < 0) AS negative_fares
FROM `{TABLE_ID}`
"""

print("Running automated BigQuery quality checks...")

result = next(iter(client.query(query).result()))

checks = {
    "Expected row count": result.total_records == EXPECTED_ROWS,
    "January date range": result.invalid_dates == 0,
    "No negative distances": result.negative_distances == 0,
}

print("\nDATA QUALITY REPORT")
print("=" * 45)

for name, passed in checks.items():
    status = "PASS" if passed else "FAIL"
    print(f"{name}: {status}")

print("\nAdditional data quality observations:")
print(f"Missing passenger counts: {result.missing_passengers}")
print(f"Negative fares: {result.negative_fares}")

if not all(checks.values()):
    raise RuntimeError("Data quality checks failed!")

print("\nALL REQUIRED DATA QUALITY CHECKS PASSED!")
