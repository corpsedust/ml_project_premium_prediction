import streamlit as st
from prediction_helper import predict

st.set_page_config("Health Insurance Prediction App", layout="centered")

# st.number_input("Age", min_value=18, max_value = 100, step = 1)
# if st.button("Predict"):
#     print("Predict clicked")



# st.set_page_config(page_title="Input Form", layout="centered")
st.title("Health Insurance Prediction App")

c1, c2, c3 = st.columns(3)

with c1:
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
    gender = st.selectbox("Gender", ["Male", "Female"])
    bmi_category = st.selectbox("BMI Category", ["Overweight", "Underweight", "Normal", "Obesity"])
    employment_status = st.selectbox("Employment Status", ["Self-Employed", "Freelancer", "Salaried"])

with c2:
    income_lakhs = st.number_input("Income (Lakhs)", min_value=1, max_value=99, step=1)
    region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])
    smoking_status = st.selectbox("Smoking Status", ["Regular", "No Smoking", "Occasional"])
    insurance_plan = st.selectbox("Insurance Plan", ["Silver", "Bronze", "Gold"])

with c3:
    number_of_dependants = st.number_input("Number of Dependants", min_value=0, max_value=5, step=1)
    genetical_risk = st.number_input("Genetical Risk", min_value=0, max_value=5, step=1)
    marital_status = st.selectbox("Marital Status", ["Unmarried", "Married"])
    medical_history = st.selectbox(
        "Medical History",
        [
            "High blood pressure",
            "No Disease",
            "Diabetes & High blood pressure",
            "Diabetes & Heart disease",
            "Diabetes",
            "Diabetes & Thyroid",
            "Heart disease",
            "Thyroid",
            "High blood pressure & Heart disease"
        ]
    )


input_value = {
        "age": age,
        "income_lakhs": income_lakhs,
        "number_of_dependants": number_of_dependants,
        "genetical_risk": genetical_risk,
        "gender": gender,
        "region": region,
        "marital_status": marital_status,
        "bmi_category": bmi_category,
        "smoking_status": smoking_status,
        "employment_status": employment_status,
        "medical_history": medical_history,
        "insurance_plan": insurance_plan
    }

if st.button("Predict"):
    prediction = float(predict(input = input_value))
    # st.dataframe(df, width='stretch')
    st.markdown(
        f"""
        <div style="
            display: flex;
            justify-content: center;
            margin-top: 30px;
        ">
            <div style="
                background-color: #1f2933;
                padding: 30px 50px;
                border-radius: 12px;
                text-align: center;
                box-shadow: 0 4px 20px rgba(0,0,0,0.4);
            ">
                <div style="font-size: 18px; color: #9ca3af;">
                    Predicted Premium
                </div>
                <div style="font-size: 42px; font-weight: 700; color: #ffffff;">
                    ₹ {prediction:,.0f}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    