import streamlit as st
from prediction_helper import predict

st.set_page_config(page_title="Health Insurance Premium Predictor", layout="wide")

st.markdown("""
<style>
* {
    margin: 0;
    padding: 0;
}

.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
    min-height: 100vh;
}

.main-header {
    text-align: center;
    padding: 2rem 0 3rem 0;
    background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
    border-radius: 0 0 20px 20px;
    margin-bottom: 2rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

.main-header h1 {
    font-size: 2.8rem;
    color: white;
    font-weight: 800;
    letter-spacing: 1px;
    margin-bottom: 0.5rem;
}

.main-header p {
    color: rgba(255,255,255,0.9);
    font-size: 1.1rem;
    font-weight: 300;
}

.section-card {
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    border: 2px solid #3b82f6;
    border-radius: 15px;
    padding: 2rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 20px rgba(59, 130, 246, 0.1);
}

.section-title {
    color: #60a5fa;
    font-size: 1.3rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.stNumberInput > div > div > input,
.stSelectbox > div > div > select,
.stSlider > div > div > div > input {
    background-color: #0f172a !important;
    color: white !important;
    border: 2px solid #3b82f6 !important;
    border-radius: 8px !important;
    padding: 0.8rem !important;
    font-size: 1rem !important;
}

.stNumberInput label,
.stSelectbox label,
.stSlider label {
    color: #e0e7ff !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
}

.stButton > button {
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    color: white !important;
    font-size: 1.2rem !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 1rem 3rem !important;
    width: 100% !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 8px 15px rgba(16, 185, 129, 0.3) !important;
    cursor: pointer !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #059669 0%, #047857 100%) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 12px 25px rgba(16, 185, 129, 0.5) !important;
}

.stButton > button:active {
    transform: translateY(0) !important;
}

.result-container {
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    border-radius: 15px;
    padding: 2.5rem;
    margin-top: 2rem;
    box-shadow: 0 15px 35px rgba(16, 185, 129, 0.3);
    animation: slideUp 0.5s ease;
}

.result-label {
    color: rgba(255,255,255,0.9);
    font-size: 1.1rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.result-value {
    color: white;
    font-size: 2.8rem;
    font-weight: 900;
    letter-spacing: 1px;
}

@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.input-row {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.5rem;
}

[data-testid="stMetric"] {
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    padding: 1.5rem;
    border-radius: 12px;
    border: 2px solid #3b82f6;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>💊 Health Insurance Premium Estimator</h1>
    <p>Get an accurate premium estimate based on your health profile</p>
</div>
""", unsafe_allow_html=True)

opts = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': ['No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure', 
                        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 
                        'Diabetes & Thyroid', 'Diabetes & Heart disease'],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">👤 Personal Information</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    age = st.number_input('🎂 Age', 18, 100, 30, step=1)

with col2:
    gender = st.selectbox('👥 Gender', opts['Gender'], label_visibility="collapsed")

with col3:
    marital = st.selectbox('💍 Marital Status', opts['Marital Status'], label_visibility="collapsed")

with col4:
    deps = st.number_input('👨‍👩‍👧‍👦 Dependants', 0, 20, 0, step=1)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">💼 Employment & Income</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    emp = st.selectbox('💼 Employment Status', opts['Employment Status'])

with col2:
    region = st.selectbox('🌍 Region', opts['Region'])

with col3:
    income = st.slider('💰 Income (Lakhs)', 0, 200, 50, step=5)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🏥 Health Profile</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    bmi = st.selectbox('📏 BMI Category', opts['BMI Category'])

with col2:
    smoke = st.selectbox('🚭 Smoking Status', opts['Smoking Status'])

with col3:
    history = st.selectbox('📋 Medical History', opts['Medical History'])

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🧬 Additional Information</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    gene = st.slider('🧬 Genetical Risk Level', 0, 5, 0, step=1)

with col2:
    plan = st.selectbox('🛡️ Insurance Plan', opts['Insurance Plan'])

st.markdown('</div>', unsafe_allow_html=True)

inp = {
    'Age': age,
    'Number of Dependants': deps,
    'Income in Lakhs': income,
    'Genetical Risk': gene,
    'Insurance Plan': plan,
    'Employment Status': emp,
    'Gender': gender,
    'Marital Status': marital,
    'BMI Category': bmi,
    'Smoking Status': smoke,
    'Region': region,
    'Medical History': history
}

if st.button('🔍 Calculate Premium', use_container_width=True):
    try:
        pr = predict(inp)
        st.markdown(f"""
        <div class="result-container">
            <div class="result-label">💵 Your Estimated Annual Premium</div>
            <div class="result-value">₹ {pr:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error in prediction: {str(e)}")
