# Data Cleaning Log

## Dataset Summary

Rows: 10

Columns: 5

## Missing Value Audit

| Column      | Null Count | Null Percent |
| ----------- | ---------- | ------------ |
| timestamp   | 0          | 0.0          |
| temperature | 0          | 0.0          |
| humidity    | 0          | 0.0          |
| co2         | 0          | 0.0          |
| yield_kg    | 0          | 0.0          |

## Duplicate Checks

Duplicate Rows Removed: 0

Duplicate Timestamps Removed: 0

## Validity Checks

Invalid Humidity Values (<0 or >100): 0

Invalid CO2 Values (<=0): 0

## Cleaning Strategy

### Temperature

Forward-fill missing values if present, otherwise median imputation.

### Humidity

Forward-fill missing values if present, otherwise median imputation.

### CO2

Forward-fill missing values if present, otherwise median imputation.

### Yield (yield_kg)

Rows with missing target values would be removed. Target values are never imputed to avoid label leakage.

## Outcome

No missing values detected.

No duplicate rows detected.

No duplicate timestamps detected.

All humidity readings are within the valid range (0–100%).

All CO2 readings are positive.

Cleaned dataset exported successfully to:

data/processed/02_cleaned.parquet
