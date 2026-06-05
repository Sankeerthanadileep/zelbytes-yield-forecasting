import pandas as pd
from pathlib import Path

RAW_FILE = Path("data/raw/polyhouse_sensors.csv")
INTERIM_FILE = Path("data/interim/01_loaded.parquet")

# Load CSV and parse timestamps
df = pd.read_csv(
    RAW_FILE,
    parse_dates=["timestamp"]
)

# Inspect dataset
print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

print("\nInfo:")
df.info()

print("\nSummary Statistics:")
print(df.describe())

# Save snapshot for cleaning stage
INTERIM_FILE.parent.mkdir(parents=True, exist_ok=True)

df.to_parquet(
    INTERIM_FILE,
    index=False
)

print(f"\nSaved snapshot to {INTERIM_FILE}")