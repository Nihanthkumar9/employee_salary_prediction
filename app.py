import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
model = pickle.load(open("income_classifier.pkl", "rb"))
encoder = pickle.load(open("encoder.pkl", "rb"))

st.set_page_config(page_title="Income Prediction App", layout="centered")

st.title("💼 Employee Income Prediction")
st.write("This app predicts whether income is >50K or <=50K based on input features.")

# --- User Inputs ---
age = st.slider("Age", 18, 90, 30)
workclass = st.selectbox("Workclass", encoder["workclass"].classes_)
education = st.selectbox("Education", encoder["education"].classes_)
marital_status = st.selectbox("Marital Status", encoder["marital-status"].classes_)
occupation = st.selectbox("Occupation", encoder["occupation"].classes_)
relationship = st.selectbox("Relationship", encoder["relationship"].classes_)
race = st.selectbox("Race", encoder["race"].classes_)
sex = st.selectbox("Sex", encoder["sex"].classes_)
hours_per_week = st.slider("Hours Per Week", 1, 100, 40)
native_country = st.selectbox("Native Country", encoder["native-country"].classes_)

# --- Prepare Input ---
input_dict = {
    "age": age,
    "workclass": encoder["workclass"].transform([workclass])[0],
    "education": encoder["education"].transform([education])[0],
    "marital-status": encoder["marital-status"].transform([marital_status])[0],
    "occupation": encoder["occupation"].transform([occupation])[0],
    "relationship": encoder["relationship"].transform([relationship])[0],
    "race": encoder["race"].transform([race])[0],
    "sex": encoder["sex"].transform([sex])[0],
    "hours-per-week": hours_per_week,
    "native-country": encoder["native-country"].transform([native_country])[0],
}

features = pd.DataFrame([input_dict])

# --- Predict ---
if st.button("🔮 Predict Income"):
    prediction = model.predict(features)[0]
    result = ">50K" if prediction == 1 else "<=50K"
    st.success(f"Predicted Income: **{result}**")
