import pandas as pd
import joblib

model_young = joblib.load(r"D:/Healthcare_premium_project/project_1_datacleaning_&_EDA_resources/app/artifacts/model_young.joblib")
model_rest = joblib.load(r"D:/Healthcare_premium_project/project_1_datacleaning_&_EDA_resources/app/artifacts/model_rest.joblib")
scaler_young = joblib.load(r"D:/Healthcare_premium_project/project_1_datacleaning_&_EDA_resources/app/artifacts/scaler_young.joblib")
scaler_rest = joblib.load(r"D:/Healthcare_premium_project/project_1_datacleaning_&_EDA_resources/app/artifacts/scaler_rest.joblib")

def calculate_normalized_risk(medical_history):
    risk_scores = {
        "diabetes": 6, "heart disease": 8, "high blood pressure": 6,
        "thyroid": 5, "no disease": 0, "none": 0
    }
    diseases = medical_history.lower().split(" & ")
    total_score = sum(risk_scores.get(d, 0) for d in diseases)
    return total_score / 14

def preprocess_input(input_dict):
    columns = [
        'age', 'number_of_dependants', 'income_lakhs', 'insurance_plan',
        'genetical_risk', 'Normalized_risk_score', 'gender_Male', 'region_Northwest',
        'region_Southeast', 'region_Southwest', 'marital_status_Unmarried',
        'bmi_category_Obesity', 'bmi_category_Overweight', 'bmi_category_Underweight',
        'smoking_status_Occasional', 'smoking_status_Regular',
        'employment_status_Salaried', 'employment_status_Self-Employed'
    ]

    plan_encode = {'Bronze': 1, 'Silver': 2, 'Gold': 3}
    df = pd.DataFrame(0, columns=columns, index=[0])

    if input_dict['Gender'] == 'Male':
        df['gender_Male'] = 1
    if input_dict['Region'] == 'Northwest':
        df['region_Northwest'] = 1
    elif input_dict['Region'] == 'Southeast':
        df['region_Southeast'] = 1
    elif input_dict['Region'] == 'Southwest':
        df['region_Southwest'] = 1
    if input_dict['Marital Status'] == 'Unmarried':
        df['marital_status_Unmarried'] = 1
    if input_dict['BMI Category'] == 'Obesity':
        df['bmi_category_Obesity'] = 1
    elif input_dict['BMI Category'] == 'Overweight':
        df['bmi_category_Overweight'] = 1
    elif input_dict['BMI Category'] == 'Underweight':
        df['bmi_category_Underweight'] = 1
    if input_dict['Smoking Status'] == 'Occasional':
        df['smoking_status_Occasional'] = 1
    elif input_dict['Smoking Status'] == 'Regular':
        df['smoking_status_Regular'] = 1
    if input_dict['Employment Status'] == 'Salaried':
        df['employment_status_Salaried'] = 1
    elif input_dict['Employment Status'] == 'Self-Employed':
        df['employment_status_Self-Employed'] = 1

    df['insurance_plan'] = plan_encode.get(input_dict['Insurance Plan'], 1)
    df['age'] = input_dict['Age']
    df['number_of_dependants'] = input_dict['Number of Dependants']
    df['income_lakhs'] = input_dict['Income in Lakhs']
    df['genetical_risk'] = input_dict['Genetical Risk']
    df['Normalized_risk_score'] = calculate_normalized_risk(input_dict['Medical History'])

    return handle_scaling(input_dict['Age'], df)

def handle_scaling(age, df):
    scaler_obj = scaler_young if age <= 25 else scaler_rest
    scaler = scaler_obj['scaler']
    cols = scaler_obj['cols_to_scale']
    df['income_level'] = 0
    df[cols] = scaler.transform(df[cols])
    return df.drop('income_level', axis=1)

def predict(input_dict):
    df = preprocess_input(input_dict)
    model = model_young if input_dict['Age'] <= 25 else model_rest
    return int(model.predict(df)[0])
