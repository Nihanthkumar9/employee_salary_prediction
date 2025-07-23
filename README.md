# Employee_Salary or Income_Prediction
# 💼 Employee Income Prediction App

This is a simple yet powerful Streamlit web app that predicts whether an individual's income is more than $50K or not based on demographic attributes. It uses a machine learning model trained on the Adult Census dataset.

## 🚀 Live Preview
Run this app locally using Streamlit to get real-time predictions.

## 🔍 Features
- Predict income class (`<=50K` or `>50K`) based on input attributes.
- Intuitive UI for quick data entry.
- Categorical features automatically encoded with pre-trained encoders.
- Built with: `Streamlit`, `scikit-learn`, `pandas`, `numpy`.

## 📊 Input Fields
- Age
- Workclass
- Education
- Marital Status
- Occupation
- Relationship
- Race
- Sex
- Hours per week
- Native Country

## 🧠 ML Model
A classification model trained using the Adult Income Dataset. Inputs are preprocessed and encoded using `LabelEncoder`. Model and encoders are loaded from `.pkl` files.

## 🛠 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/employee-income-prediction.git
   cd employee-income-prediction
2.Install dependencies:
  pip install -r requirements.txt
3.Run the Streamlit app:
  streamlit run app.py
🗂 Files in This Repo
app.py – Streamlit frontend and prediction logic.

income_classifier.pkl – Trained classification model.

encoder.pkl – LabelEncoders for categorical fields.

README.md – Project documentation.

requirements.txt – Required Python libraries.


💡 Inspiration
---
Inspired by real-world HR analytics problems where organizations want to understand employee income brackets based on socio-economic factors.


Contributions and feedback are welcome!

---

### ✅ `requirements.txt`

You should include a `requirements.txt` like this in the repo:

```txt
streamlit
scikit-learn
pandas
numpy

