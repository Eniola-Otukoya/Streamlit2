import streamlit as st
import joblib
import pandas as pd
import numpy as np

model = joblib.load('financial_inclusion_le.pkl')

feature_names = [
    'year', 'household_size', 'age_of_respondent', 
    'country_Rwanda', 'country_Tanzania', 'country_Uganda',
    'location_type_Urban', 'cellphone_access_Yes', 
    'gender_of_respondent_Male', 
    'relationship_with_head_Head of Household', 'relationship_with_head_Other non-relatives', 
    'relationship_with_head_Other relative', 'relationship_with_head_Parent', 'relationship_with_head_Spouse', 
    'marital_status_Dont know', 'marital_status_Married/Living together', 'marital_status_Single/Never Married', 
    'marital_status_Widowed', 
    'education_level_Other/Dont know/RTA', 'education_level_Primary education', 
    'education_level_Secondary education', 'education_level_Tertiary education', 'education_level_Vocational/Specialised training', 
    'job_type_Farming and Fishing', 'job_type_Formally employed Government', 'job_type_Formally employed Private', 
    'job_type_Government Dependent', 'job_type_Informally employed', 'job_type_No Income', 'job_type_Other Income', 
    'job_type_Remittance Dependent', 'job_type_Self employed'
]

st.title("Financial Inclusion Prediction App")

st.header("Enter Feature Values")
year = st.number_input("Year", min_value=2000, max_value=2023, value=2020)
household_size = st.number_input("Household Size", min_value=1, max_value=20, value=5)
age_of_respondent = st.number_input("Age of Respondent", min_value=16, max_value=100, value=30)

country = st.selectbox("Country", ["Rwanda", "Tanzania", "Uganda"])
location_type = st.selectbox("Location Type", ["Urban", "Rural"])
cellphone_access = st.selectbox("Cellphone Access", ["Yes", "No"])
gender = st.selectbox("Gender", ["Male", "Female"])
relationship_with_head = st.selectbox("Relationship with Head", ["Head of Household", "Other non-relatives", "Other relative", "Parent", "Spouse"])
marital_status = st.selectbox("Marital Status", ["Dont know", "Married/Living together", "Single/Never Married", "Widowed"])
education_level = st.selectbox("Education Level", ["Other/Dont know/RTA", "Primary education", "Secondary education", "Tertiary education", "Vocational/Specialised training"])
job_type = st.selectbox("Job Type", [
     "Farming and Fishing", "Formally employed Government", "Formally employed Private", "Government Dependent", 
     "Informally employed", "No Income", "Other Income", "Remittance Dependent", "Self employed"
 ])


input_dict = {feature: 0 for feature in feature_names}  

input_dict['year'] = year
input_dict['household_size'] = household_size
input_dict['age_of_respondent'] = age_of_respondent

input_dict[f'country_{country}'] = 1
input_dict[f'location_type_{location_type}'] = 1
input_dict[f'cellphone_access_{cellphone_access}'] = 1
input_dict[f'gender_of_respondent_{gender}'] = 1
input_dict[f'relationship_with_head_{relationship_with_head}'] = 1
input_dict[f'marital_status_{marital_status}'] = 1
input_dict[f'education_level_{education_level}'] = 1
input_dict[f'job_type_{job_type}'] = 1

input_data = pd.DataFrame([input_dict])

if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write(f"Prediction: {'Has Bank Account' if prediction[0] == 1 else 'No Bank Account'}")