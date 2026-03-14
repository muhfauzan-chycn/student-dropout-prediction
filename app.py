import streamlit as st
import pandas as pd
import joblib

# Load model 
@st.cache_resource
def load_model():
    return joblib.load("model/model_dropout.pkl")

model = load_model()

st.title("🎓 Student Dropout Prediction System")

st.write(
"""
This system predicts the **Risk of Student Dropout** based on academic performance and demographic information
"""
)

st.divider()

st.header("Student Information")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age at Enrollment",
        min_value=15,
        max_value=70,
        value=20
    )

    admission_grade = st.number_input(
        "Admission Grade",
        min_value=0.0,
        max_value=200.0
    )

    scholarship_option = st.selectbox(
        "Scholarship Holder",
        ["No","Yes"]
    )

with col2:

    first_sem_approved = st.number_input(
        "Approved Courses (1st Semester)",
        min_value=0
    )

    second_sem_approved = st.number_input(
        "Approved Course (2nd Semester)",
        min_value=0
    )

    gender_option = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

# Encoding input
scholarship = 1 if scholarship_option == "Yes" else 0
gender = 1 if gender_option == "Male" else 0

if st.button("Predict Dropout Risk"):
    
    input_data = pd.DataFrame({
        "Age_at_enrollment":[age],
        "Admission_grade":[admission_grade],
        "Curricular_units_1st_sem_approved":[first_sem_approved],
        "Curricular_units_2nd_sem_approved":[second_sem_approved],
        "Scholarship_holder":[scholarship],
        "Gender":[gender]
    })

    prediction = model.predict(input_data)

    probability = model.predict_proba(input_data)[0][1]

    st.divider()
    st.subheader("Prediction Result")

    if prediction[0] == 1:

        st.error("⚠ High Risk of Dropout")

    else:

        st.success("✅ Low Risk of Dropout")
    
    st.write(f"Dropout Probability: **{probability*100:.2f}%**")