import pandas as pd
import numpy as np

np.random.seed(42)

n = 100

timestamps = pd.date_range(
    start="2026-06-01 08:00:00",
    periods=n,
    freq="h"
)

df = pd.DataFrame({
    "timestamp": timestamps,
    "temperature": np.round(np.random.normal(25, 1.5, n), 1),
    "humidity": np.round(np.random.normal(85, 4, n), 0),
    "co2": np.round(np.random.normal(900, 80, n), 0),
    "yield_kg": np.round(np.random.normal(13, 0.8, n), 2)
})

df.to_csv(
    "data/raw/polyhouse_sensors.csv",
    index=False
)

print("100-row dataset created.")