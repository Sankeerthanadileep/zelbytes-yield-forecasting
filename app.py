import streamlit as st
import joblib
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Zelbytes Yield Forecasting",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load model once
@st.cache_resource
def load_model():
    return joblib.load("models/random_forest.joblib")

model = load_model()

# Title
st.title("🌱 Zelbytes Yield Forecasting")

st.write(
    "Predict crop yield using temperature, humidity, and CO₂ sensor readings."
)

# Sidebar inputs
st.sidebar.header("Sensor Inputs")

temperature = st.sidebar.slider(
    "Temperature (°C)",
    min_value=15.0,
    max_value=40.0,
    value=25.0
)

humidity = st.sidebar.slider(
    "Humidity (%)",
    min_value=20.0,
    max_value=100.0,
    value=60.0
)

co2 = st.sidebar.slider(
    "CO₂ (ppm)",
    min_value=300,
    max_value=1500,
    value=800
)

# Prediction
if st.button("Predict Yield"):

    input_data = pd.DataFrame({
        "temperature": [temperature],
        "humidity": [humidity],
        "co2": [co2],
        "temp_humidity": [temperature * humidity]
    })

    prediction = model.predict(input_data)[0]

    st.metric(
        label="Predicted Yield",
        value=f"{prediction:.2f} kg"
    )

    # Humidity Sensitivity Analysis
    st.subheader("Humidity Sensitivity Analysis")

    humidities = []
    predictions = []

    for h in range(20, 101, 5):

        temp_df = pd.DataFrame({
            "temperature": [temperature],
            "humidity": [h],
            "co2": [co2],
            "temp_humidity": [temperature * h]
        })

        pred = model.predict(temp_df)[0]

        humidities.append(h)
        predictions.append(pred)

    chart_df = pd.DataFrame({
        "Humidity": humidities,
        "Predicted Yield": predictions
    })

    st.line_chart(chart_df.set_index("Humidity"))

    # Model Information
    st.subheader("Model Information")

    with st.expander("View Details"):
        st.write("Model Version: v1.0")
        st.write("Champion Model: Random Forest")
        st.write("MAE: 0.49")