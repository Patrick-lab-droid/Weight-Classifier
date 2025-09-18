import streamlit as st
import requests

st.title("Obesity Prediction")

gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=0, max_value=60, value=25)
height = st.number_input("Height (m)", min_value=1.0, max_value=2.5, value=1.70)
weight = st.number_input("Weight (kg)", min_value=20.0, max_value=200.0, value=70.0)
family_history = st.selectbox("Family History of Overweight", ["yes", "no"])
favc = st.selectbox("Frequent High Calorie Food (FAVC)", ["yes", "no"])
fcvc = st.slider("Frequency of Vegetable Consumption (FCVC)", 1.0, 3.0, 2.0, step= 0.01)
ncp = st.slider("Number of Main Meals (NCP)", 1.0, 4.0, 3.0, step=0.01)
caec = st.selectbox("Eating Between Meals (CAEC)", ["no", "Sometimes", "Frequently", "Always"])
smoke = st.selectbox("Do you smoke?", ["yes", "no"])
ch2o = st.slider("Water Intake (CH2O)", 1.0, 3.0, 2.0, step=0.01)
scc = st.selectbox("Do you monitor calories (SCC)?", ["yes", "no"])
faf = st.slider("Physical Activity Frequency (FAF)", 0.0, 3.0, 1.0, step=0.01)
tue = st.slider("Technology Usage (TUE)", 0.0, 3.0, 1.0, step=0.001)
calc = st.selectbox("Alcohol Consumption (CALC)", ["no", "Sometimes", "Frequently", "Always"])
mtrans = st.selectbox("Transportation Mode (MTRANS)", ["Public_Transportation", "Walking", "Motorbike", "Bike", "Automobile"])

if st.button("Predict"):
    payload = {
        "Gender": gender,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "family_history_with_overweight": family_history,
        "FAVC": favc,
        "FCVC": fcvc,
        "NCP": ncp,
        "CAEC": caec,
        "SMOKE": smoke,
        "CH2O": ch2o,
        "SCC": scc,
        "FAF": faf,
        "TUE": tue,
        "CALC": calc,
        "MTRANS": mtrans
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=payload)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {result['prediction']}")
    else:
        st.error("Prediction failed. Please check the API.")
