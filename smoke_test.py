import pandas as pd

sensor_row = {
    "temperature": 24.5,
    "humidity": 87,
    "co2": 950,
    "yield": 2.8
}

df = pd.DataFrame([sensor_row])

print("Sample Polyhouse Sensor Data")
print(df)