import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from joblib import load
import streamlit as st

# Import Model
model = load("model/gboost.joblib")
scaler = load("model/scaler.joblib")

columns_to_scale = [
    "Admission grade",
    "Curricular units 1st sem (approved)",
    "Curricular units 1st sem (grade)",
    "Curricular units 2nd sem (approved)",
    "Curricular units 2nd sem (grade)",
    "Age at enrollment",
]

categorical_cols = [
    "Debtor",
    "Scholarship holder",
    "Tuition fees up to date",
    "Application mode",
    "Marital status",
    "Course"
]

# Hardcoded label encoder classes based on training data
label_encoder_classes = {
    "Debtor": ["No", "Yes"],
    "Scholarship holder": ["No", "Yes"],
    "Tuition fees up to date": ["No", "Yes"],
    "Application mode": [
        "1st phase - general contingent",
        "1st phase - special contingent (Azores Island)",
        "1st phase - special contingent (Madeira Island)",
        "2nd phase - general contingent",
        "3rd phase - general contingent",
        "Change of course",
        "Change of institution/course",
        "Change of institution/course (International)",
        "Holders of other higher courses",
        "International student (bachelor)",
        "Ordinance No. 533-A/99, item b2 (Different Plan)",
        "Ordinance No. 533-A/99, item b3 (Other Institution)",
        "Ordinance No. 612/93",
        "Ordinance No. 854-B/99",
        "Over 23 years old",
        "Short cycle diploma holders",
        "Technological specialization diploma holders",
        "Transfer"
    ],
    "Marital status": [
        "Divorced",
        "Facto Union",
        "Legally Separated",
        "Married",
        "Single",
        "Widower"
    ],
    "Course": [
        "Agronomy",
        "Animation and Multimedia Design",
        "Basic Education",
        "Biofuel Production Technologies",
        "Communication Design",
        "Equinculture",
        "Informatics Engineering",
        "Journalism and Communication",
        "Management",
        "Management (evening attendance)",
        "Nursing",
        "Oral Hygiene",
        "Advertising and Marketing Management",
        "Social Service",
        "Social Service (evening attendance)",
        "Tourism",
        "Veterinary Nursing"
    ]
}

label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    le.classes_ = np.array(label_encoder_classes[col])  # ubah list ke array
    label_encoders[col] = le

# Set Streamlit page config
st.set_page_config(
    page_title="Prediksi Mahasiswa Dropout", layout="wide"
)


def preprocess_data(df):
    processed_df = df.copy()

    # Encode categorical columns using predefined encoders
    for col in categorical_cols:
        processed_df[col] = label_encoders[col].transform(processed_df[col])

    # Perform Min-Max scaling for numerical columns
    processed_df[columns_to_scale] = scaler.transform(processed_df[columns_to_scale])

    return processed_df


def main():
    st.title("Student Dropout Predictor")
    st.subheader("Input Student Information:")

    input_data = {}
    col1, col2, col3 = st.columns(3)
    with col1:
        input_data["Debtor"] = st.radio("Select Debtor:", label_encoder_classes["Debtor"])
    with col2:
        input_data["Scholarship holder"] = st.radio("Scholarship holder:", label_encoder_classes["Scholarship holder"])
    with col3:
        input_data["Tuition fees up to date"] = st.radio("Tuition fees up to date:", label_encoder_classes["Tuition fees up to date"])

    col1, col2, col3 = st.columns(3)
    with col1:
        input_data["Marital status"] = st.selectbox("Marital status", label_encoder_classes["Marital status"])
    with col2:
        input_data["Application mode"] = st.selectbox("Application mode", label_encoder_classes["Application mode"])
    with col3:
        input_data["Course"] = st.selectbox("Course", label_encoder_classes["Course"])

    col1, col2, col3 = st.columns(3)
    with col1:
        input_data["Admission grade"] = st.number_input("Admission grade:", min_value=0.0, max_value=200.0, value=100.0, step=1.0)
        input_data["Curricular units 1st sem (approved)"] = st.number_input("Approve 1st Sem:", min_value=0.0, max_value=26.0, value=5.0, step=1.0)
    with col2:
        input_data["Curricular units 1st sem (grade)"] = st.number_input("1st Sem grade:", min_value=0.0, max_value=18.0, value=12.0, step=0.5)
        input_data["Curricular units 2nd sem (approved)"] = st.number_input("Approve 2nd Sem:", min_value=0.0, max_value=20.0, value=5.0, step=1.0)
    with col3:
        input_data["Curricular units 2nd sem (grade)"] = st.number_input("2nd Sem grade:", min_value=0.0, max_value=18.0, value=12.0, step=0.5)
        input_data["Age at enrollment"] = st.number_input("Age at enrollment:", min_value=18.0, max_value=70.0, value=18.0, step=1.0)

    input_df = pd.DataFrame([input_data])

    if st.button("Predict"):
        final_df = preprocess_data(input_df)
        prediction = model.predict(final_df)[0]

        label_map = {0: "Dropout", 1: "Enrolled", 2: "Graduate"}
        st.success(f"Prediction: {label_map.get(prediction, 'Unknown')}")
        
        st.write("Encoded input:", final_df)


if __name__ == "__main__":
    main()
