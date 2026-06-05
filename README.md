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
