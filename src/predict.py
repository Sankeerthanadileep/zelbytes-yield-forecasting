import json
import joblib
import pandas as pd
from pathlib import Path

# Project root
ROOT_DIR = Path(__file__).resolve().parent.parent

# Load artifacts
MODEL_PATH = ROOT_DIR / "models" / "champion.joblib"
SCALER_PATH = ROOT_DIR / "models" / "scaler.joblib"
FEATURES_PATH = ROOT_DIR / "models" / "feature_columns.json"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

with open(FEATURES_PATH, "r") as f:
    feature_columns = json.load(f)


def make_prediction(temperature, humidity, co2):
    """
    Predict crop yield in kg.
    """

    data = pd.DataFrame(
        [[temperature, humidity, co2]],
        columns=feature_columns
    )

    scaled_data = scaler.transform(data)

    prediction = model.predict(scaled_data)[0]

    return float(round(prediction, 2))


if __name__ == "__main__":
    pred = make_prediction(
        temperature=25,
        humidity=70,
        co2=450
    )

    print(f"Predicted Yield: {pred} kg")