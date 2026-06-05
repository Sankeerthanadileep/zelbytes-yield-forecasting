import pandas as pd

# Load data
df = pd.read_parquet(
    "data/interim/01_loaded.parquet"
)

print("\nDataset Shape:")
print(df.shape)

# Missing values
audit = pd.DataFrame({
    "null_count": df.isnull().sum(),
    "null_percent": (
        df.isnull().mean() * 100
    ).round(2)
})

print("\nMissing Value Audit:")
print(audit)

# Duplicate rows
duplicate_rows = df.duplicated().sum()

print("\nDuplicate Rows:")
print(duplicate_rows)

# Duplicate timestamps
duplicate_timestamps = (
    df["timestamp"]
    .duplicated()
    .sum()
)

print("\nDuplicate Timestamps:")
print(duplicate_timestamps)

# Humidity validity check
invalid_humidity = (
    (df["humidity"] < 0) |
    (df["humidity"] > 100)
).sum()

print("\nInvalid Humidity Values:")
print(invalid_humidity)

# CO2 validity check
invalid_co2 = (
    df["co2"] <= 0
).sum()

print("\nInvalid CO2 Values:")
print(invalid_co2)

# Save cleaned dataset
df.to_parquet(
    "data/processed/02_cleaned.parquet",
    index=False
)

print("\nCleaned dataset saved.")

# Save cleaned CSV version
df.to_csv(
    "data/processed/02_cleaned.csv",
    index=False
)

print("Cleaned CSV saved.")