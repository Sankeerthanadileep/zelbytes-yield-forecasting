# Zelbytes Yield Forecasting

## Environment Setup

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install pandas numpy matplotlib scikit-learn jupyter streamlit joblib
```

### Run Smoke Test

```bash
python smoke_test.py
```

Expected Output:

```text
Sample Polyhouse Sensor Data
   temperature  humidity  co2  yield
0         24.5        87  950    2.8
```

## Project Structure

```text
data/
├── raw/
├── processed/

notebooks/
src/
models/

smoke_test.py
README.md
```
## Task 4: Feature Engineering & Temporal Train/Test Split

### Features Used

* temperature
* humidity
* co2
* temp_humidity (engineered feature = temperature × humidity)

### Target Variable

* yield_kg

### Train/Test Split

* Total Rows: 100
* Train Rows: 80
* Test Rows: 20

#### Training Period

* Start: 2026-06-01 08:00:00
* End: 2026-06-04 15:00:00

#### Testing Period

* Start: 2026-06-04 16:00:00
* End: 2026-06-05 11:00:00

### Scaling

* MinMaxScaler used for feature scaling
* Scaler fitted only on training data
* Same scaler applied to test data
* Data leakage prevented

### Saved Artifacts

* models/scaler.joblib
* data/processed/X_train.csv
* data/processed/X_test.csv
* data/processed/y_train.csv
* data/processed/y_test.csv
