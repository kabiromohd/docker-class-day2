import requests
import streamlit as st


# Flask API endpoint
API_URL = "http://localhost:9690/predict"


# Page configuration
st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="centered"
)


st.title("🩺 Diabetes Prediction")
st.write("Enter the patient's information below to predict their diabetic status.")


# Patient information
gender = st.selectbox(
    "Gender",
    options=["F", "M"]
)

age = st.number_input(
    "Age",
    min_value=1.0,
    max_value=120.0,
    value=50.0
)

urea = st.number_input(
    "Urea",
    min_value=0.0,
    value=4.7
)

cr = st.number_input(
    "Creatinine (Cr)",
    min_value=0.0,
    value=46.0
)

hba1c = st.number_input(
    "HbA1c",
    min_value=0.0,
    value=4.9
)

chol = st.number_input(
    "Cholesterol (Chol)",
    min_value=0.0,
    value=4.2
)

tg = st.number_input(
    "Triglycerides (TG)",
    min_value=0.0,
    value=0.9
)

hdl = st.number_input(
    "HDL",
    min_value=0.0,
    value=2.4
)

ldl = st.number_input(
    "LDL",
    min_value=0.0,
    value=1.4
)

vldl = st.number_input(
    "VLDL",
    min_value=0.0,
    value=0.5
)

bmi = st.number_input(
    "BMI",
    min_value=0.0,
    value=24.0
)


# Prediction
if st.button("Predict", type="primary"):

    client = {
        "Gender": gender,
        "AGE": age,
        "Urea": urea,
        "Cr": cr,
        "HbA1c": hba1c,
        "Chol": chol,
        "TG": tg,
        "HDL": hdl,
        "LDL": ldl,
        "VLDL": vldl,
        "BMI": bmi
    }

    try:
        response = requests.post(
            API_URL,
            json=client,
            timeout=10
        )

        response.raise_for_status()

        result = response.json()

        predictions = {
            0: "Patient not diabetic",
            1: "Patient diabetic",
            2: "Patient probable diabetic"
        }

        status = result["Predicted diabetic Status"]

        prediction = predictions.get(status, "Unknown")

        st.success(f"Prediction: {prediction}")

    except requests.exceptions.RequestException as e:
        st.error(f"Could not connect to the prediction API: {e}")