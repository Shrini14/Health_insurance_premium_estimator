# 🏥 Health Insurance Premium Predictor

🎯 **Live Demo:** [Click here to try the app!](https://premiumpulse.streamlit.app/)  
🚀 Powered by **XGBoost** | 🧠 Model Segmentation | 🎨 Colorful UI

---

## 🔥 Why This Project?

Initially, one XGBoost model gave **98% accuracy** but struggled for users **<= 25 years old** — with **73% predictions having >10% error**.

So I:
- 🔍 Performed error analysis
- 🧬 Collected extra data for the younger group (new feature: `genetical_risk`)
- 🧠 Trained a separate model for that segment
- ✅ Brought error down from **73% → 2%**
- 📊 Maintained 98–99% accuracy across both segments

---

## 🧠 Model Architecture

| Age Group        | Model      | Accuracy | Special Features          |
|------------------|------------|----------|---------------------------|
| `<= 25`           | LinearRegression    | 98%      | Includes `genetical_risk` |
| `> 25`          | XGBoost    | 99%      | Standard features only     |

🧪 Normalized Risk Score is calculated from medical history dynamically.

---

## 💡 Features Used

- Age
- Genetical Risk (for age < 25)
- Income in Lakhs
- Insurance Plan (Bronze/Silver/Gold)
- Normalized Risk Score
- BMI Category
- Region
- Employment Type
- Smoking Status
- Medical History
- Marital Status
- Gender

---

## 📊 Feature Importance

### 👶 Young Age Group (≤ 25)

| 🧠 Feature                | 🔥 Importance     |
| ------------------------- | ----------------- |
| **Normalized Risk Score** | ██████████ (High) |
| **Income (Lakhs)**        | ████████▍         |
| **Genetical Risk**        | ███████▍          |
| **BMI: Obesity**          | █████▎            |
| **Insurance Plan**        | █████             |
| **Employment: Salaried**  | ████              |
| **Region: Northwest**     | ███               |
| **Marital: Unmarried**    | ██                |
| **Smoking: Occasional**   | ██                |
| **Others**                | ░░ (Minor Impact) |

#### After introducing Genetical Risk, the error rate for young users dropped dramatically from 73% ➝ 2%.


### 👴 Rest Age Group (> 25)

| 🧠 Feature                | 🔥 Importance     |
| ------------------------- | ----------------- |
| **Income (Lakhs)**        | ██████████ (High) |
| **Insurance Plan**        | ████████▍         |
| **Normalized Risk Score** | ███████           |
| **Age**                   | █████▎            |
| **Employment: Salaried**  | ████              |
| **Smoking: Regular**      | ███▍              |
| **BMI: Overweight**       | ███               |
| **Gender: Male**          | ██                |
| **Region: Southwest**     | ██                |
| **Others**                | ░░ (Minor Impact) |


#### ⚙️ No extra features were needed. XGBoost alone gave 99% accuracy for users aged over 25.

---

## 🌐 Live Web App

💻 App hosted on **Streamlit Cloud**

🔗 [👉 Try the Predictor Now](https://premiumpulse.streamlit.app/)

---

## ⚙️ How to Run Locally
```bash
git clone https://github.com/Shrini14/ml-project-health_insurance_premium_estimator
cd ml-project-health_insurance_premium_estimator
pip install -r requirements.txt
streamlit run app/main.py
```
---

## 📁 Folder Structure
ml-project-health_insurance_premium_estimator/
│
├── app/
│   ├── main.py
│   ├── prediction_helper.py
│   └── artifacts/
├── requirements.txt
└── README.md

---

### 🧑‍💻 Developer
**R. Shrinivass**
(Data Scientist)
📬 LinkedIn: https://www.linkedin.com/in/shrinivassraju14/

---

# ⭐ Show some ❤️ by starring this repo!





