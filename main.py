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
    background: linear-gradient(135deg, #f0f9ff 0%, #f5f3ff 50%, #fef3c7 100%);
    min-height: 100vh;
}

.main-header {
    text-align: center;
    padding: 2.5rem 2rem 3rem 2rem;
    background: linear-gradient(135deg, #ff6b6b 0%, #ff8787 50%, #ffa5a5 100%);
    border-radius: 20px;
    margin: 1.5rem;
    margin-bottom: 2rem;
    box-shadow: 0 15px 35px rgba(255, 107, 107, 0.2);
}

.main-header h1 {
    font-size: 2.8rem;
    color: white;
    font-weight: 800;
    letter-spacing: 1px;
    margin-bottom: 0.5rem;
    text-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.main-header p {
    color: rgba(255,255,255,0.95);
    font-size: 1.1rem;
    font-weight: 500;
}

.section-card {
    background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 100%);
    border: 2px solid #ffa5a5;
    border-radius: 18px;
    padding: 2.2rem;
    margin: 0 1.5rem 1.5rem 1.5rem;
    box-shadow: 0 10px 30px rgba(255, 107, 107, 0.08);
    transition: all 0.3s ease;
}

.section-card:hover {
    box-shadow: 0 15px 40px rgba(255, 107, 107, 0.12);
    transform: translateY(-2px);
}

.section-title {
    color: #ff6b6b;
    font-size: 1.4rem;
    font-weight: 800;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 0.7rem;
}

.stNumberInput > div > div > input,
.stSelectbox > div > div > select,
.stSlider > div > div > div > input {
    background-color: #ffffff !important;
    color: #1a202c !important;
    border: 2.5px solid #ffb3ba !important;
    border-radius: 10px !important;
    padding: 0.9rem !important;
    font-size: 1rem !important;
    transition: all 0.3s ease !important;
}

.stNumberInput > div > div > input:focus,
.stSelectbox > div > div > select:focus,
.stSlider > div > div > div > input:focus {
    border-color: #ff6b6b !important;
    box-shadow: 0 0 0 3px rgba(255, 107, 107, 0.1) !important;
}

.stNumberInput label,
.stSelectbox label,
.stSlider label {
    color: #d32f2f !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
}

.stButton > button {
    background: linear-gradient(135deg, #ff6b6b 0%, #ff5252 50%, #ff8787 100%) !important;
    color: white !important;
    font-size: 1.2rem !important;
    font-weight: 800 !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 1.1rem 3rem !important;
    width: 100% !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 10px 25px rgba(255, 107, 107, 0.3) !important;
    cursor: pointer !important;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #ff5252 0%, #ff3838 50%, #ff6b6b 100%) !important;
    transform: translateY(-3px) !important;
    box-shadow: 0 15px 35px rgba(255, 107, 107, 0.5) !important;
}

.stButton > button:active {
    transform: translateY(-1px) !important;
}

.result-container {
    background: linear-gradient(135deg, #ffd89b 0%, #ffb366 50%, #ff9a76 100%);
    border-radius: 18px;
    padding: 3rem 2.5rem;
    margin: 2rem 1.5rem;
    box-shadow: 0 15px 40px rgba(255, 107, 107, 0.25);
    animation: slideUp 0.5s ease;
    border: 3px solid #ff8787;
    text-align: center;
}

.result-label {
    color: white;
    font-size: 1.2rem;
    font-weight: 700;
    margin-bottom: 1rem;
    text-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.result-value {
    color: white;
    font-size: 3.5rem;
    font-weight: 900;
    letter-spacing: 2px;
    text-shadow: 0 3px 8px rgba(0,0,0,0.15);
}

@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.info-box {
    background: linear-gradient(135deg, #fff5f7 0%, #fff0f3 100%);
    border-left: 5px solid #ff6b6b;
    padding: 1.2rem;
    border-radius: 8px;
    margin: 1rem 0;
}

.info-box p {
    color: #d32f2f;
    font-weight: 600;
    margin: 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>💊 Health Insurance Premium Estimator</h1>
    <p>✨ Get an accurate premium estimate based on your health profile ✨</p>
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

col1, col2, col3, col4 = st.columns(4, gap="medium")

with col1:
    age = st.number_input('🎂 Age', 18, 100, 30, step=1)

with col2:
    gender = st.selectbox('👥 Gender', opts['Gender'])

with col3:
    marital = st.selectbox('💍 Marital Status', opts['Marital Status'])

with col4:
    deps = st.number_input('👨‍👩‍👧‍👦 Dependants', 0, 20, 0, step=1)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">💼 Employment & Income</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    emp = st.selectbox('💼 Employment Status', opts['Employment Status'])

with col2:
    region = st.selectbox('🌍 Region', opts['Region'])

with col3:
    income = st.slider('💰 Income (Lakhs)', 0, 200, 50, step=5)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🏥 Health Profile</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    bmi = st.selectbox('📏 BMI Category', opts['BMI Category'])

with col2:
    smoke = st.selectbox('🚭 Smoking Status', opts['Smoking Status'])

with col3:
    history = st.selectbox('📋 Medical History', opts['Medical History'])

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🧬 Additional Information</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="medium")

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
        st.error(f"❌ Error in prediction: {str(e)}")
