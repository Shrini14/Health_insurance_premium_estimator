import streamlit as st
from prediction_helper import predict

st.set_page_config(page_title="Health Insurance Premium Predictor", layout="wide")

st.markdown("""
<style>
.stApp {
  background: linear-gradient(135deg, #fffde7, #e1f5fe);
  min-height: 100vh;
}
.title {
  font-size: 3rem;
  color: #0D47A1;
  text-align: center;
  margin-bottom: 1rem;
}
.stButton > button {
  background-color: #4CAF50;
  color: white;
  font-size: 1.1em;
  border-radius: 8px;
  padding: 0.8em 2em;
}
.stButton > button:hover {
  background-color: #388E3C;
}
.result {
  background-color: #E8F5E9;
  padding: 20px;
  border-radius: 12px;
  border-left: 8px solid #43A047;
  font-size: 1.5rem;
  color: #1B5E20;
  margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>💊 Health Insurance Premium Estimator</div>", unsafe_allow_html=True)

opts = {
  'Gender':['Male','Female'], 'Marital Status':['Unmarried','Married'],
  'BMI Category':['Normal','Obesity','Overweight','Underweight'],
  'Smoking Status':['No Smoking','Regular','Occasional'],
  'Employment Status':['Salaried','Self-Employed','Freelancer'],
  'Region':['Northwest','Southeast','Northeast','Southwest'],
  'Medical History':['No Disease','Diabetes','High blood pressure','Diabetes & High blood pressure','Thyroid',
                     'Heart disease','High blood pressure & Heart disease','Diabetes & Thyroid','Diabetes & Heart disease'],
  'Insurance Plan':['Bronze','Silver','Gold']
}

c1, c2, c3 = st.columns(3)
with c1:
    age = st.number_input('🎂 Age',18,100,18)
    gender = st.selectbox('Gender',opts['Gender'])
    bmi = st.selectbox('BMI Category',opts['BMI Category'])
    smoke = st.selectbox('Smoking Status',opts['Smoking Status'])

with c2:
    deps = st.number_input('Dependants',0,20,0)
    marital = st.selectbox('Marital Status',opts['Marital Status'])
    emp = st.selectbox('Employment Status',opts['Employment Status'])
    region = st.selectbox('Region',opts['Region'])

with c3:
    income = st.slider('💰 Income (Lakhs)',0,200,50)
    gene = st.slider('🧬 Genetical Risk',0,5,0)
    plan = st.selectbox('Insurance Plan',opts['Insurance Plan'])
    history = st.selectbox('Medical History',opts['Medical History'])

inp = {
    'Age':age, 'Number of Dependants':deps, 'Income in Lakhs':income,
    'Genetical Risk':gene, 'Insurance Plan':plan, 'Employment Status':emp,
    'Gender':gender, 'Marital Status':marital, 'BMI Category':bmi,
    'Smoking Status':smoke,'Region':region,'Medical History':history
}

if st.button('🔍 Predict Premium'):
    pr = predict(inp)
    st.markdown(f"<div class='result'>🧾 Estimated Premium: ₹ {pr:,}</div>", unsafe_allow_html=True)
