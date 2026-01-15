
import pandas as pd
import joblib
from joblib import load
import streamlit as st
import numpy as np



def preprocess_input(input_dict):
    expected_columns = ['age', 'number_of_dependants', 'bmi_category', 'smoking_status',
       'income_lakhs', 'insurance_plan', 'genetical_risk',
       'normalized_risk_score', 'gender_Male', 'region_Northwest',
       'region_Southeast', 'region_Southwest', 'marital_status_Unmarried',
       'employment_status_Salaried', 'employment_status_Self-Employed']
    
    bmi_map = {
        'Underweight' : 0, 
        'Normal' : 1,
        'Overweight' : 2,
        'Obesity' :3
    }
    
    smoking_map = {
        'No Smoking' : 0,
        'Occasional' : 1,
        'Regular' : 2
    }
    
    insurance_map = {
        'Bronze' : 0,
        'Silver' : 1,
        'Gold' : 2
    }
    # I cannot convert the incoming data into a df and then apply prprocessing logic combined because I only 
    # get single row input at a time so baat nhi banegi if you have to do onehotencoding. 
    
    risk_scores = {
        'diabetes' : 6,
        'heart disease' : 8,
        'high blood pressure' : 6,
        'thyroid' : 5,
        'no disease' : 0,
        'none' : 0
    }
        
    df = pd.DataFrame(0, columns=expected_columns, index = [0])
    
    # for key, values in input_dict:
    df['age'] = input_dict["age"]
    df['number_of_dependants'] = input_dict['number_of_dependants']
    df['bmi_category'] = bmi_map[input_dict["bmi_category"]]
    df['smoking_status'] = smoking_map[input_dict["smoking_status"]]
    df['income_lakhs'] = input_dict['income_lakhs']
    df['insurance_plan'] = insurance_map[input_dict["insurance_plan"]]
    df['genetical_risk'] = input_dict['genetical_risk']
    
    disease = input_dict['medical_history'].lower().split(" & ")
    risk_score = 0
    for  i in disease:
        risk_score = risk_score+risk_scores[i]
        
    risk_score_scaler = load("artifacts/risk_score_scaler.joblib")
    df['normalized_risk_score'] = risk_score_scaler.transform(np.array(risk_score).reshape(-1,1)).round(2)
    
    if input_dict['gender'] == 'Male':
        df['gender_Male'] = 1
        
    if input_dict['region'] == 'Northwest':
        df['region_Northwest'] = 1
    elif input_dict['region'] == 'Southeast':
        df['region_Southeast'] = 1
    elif input_dict['region'] == 'Southwest':
        df['region_Southwest'] = 1
        
        
    if input_dict['marital_status'] == 'Unmarried':
        df['marital_status_Unmarried'] = 1
        
        
    if input_dict['employment_status'] == 'Salaried':
        df['employment_status_Salaried'] = 1
        
    elif input_dict['employment_status'] == 'Self-Employed':
        df['employment_status_Self-Employed'] = 1
    
    
    young_scaler_file = load("artifacts/scaler_young.joblib")
    old_scaler_file = load("artifacts/scaler_old.joblib")
    
    
    if input_dict['age'] <= 25:
        cols = young_scaler_file['col_to_scale']
        scaler = young_scaler_file['scaler']
        df[cols] = scaler.transform(df[cols])
    
    if input_dict['age'] > 25:
        cols = old_scaler_file['col_to_scale']
        scaler = old_scaler_file['scaler']
        df[cols] = scaler.transform(df[cols])
        

    
    # if df.columns.to_list() == expected_columns:
    #     st.write("Great Success !!!")
    
    
    
    
    
    return df




def predict(input):
    df = preprocess_input(input_dict = input)
    model_old = load("artifacts\model_old.joblib")
    model_young = load("artifacts\model_young.joblib")
    prediction = 0
    if input['age'] <= 25:
        prediction = model_young.predict(df)
    elif input['age'] > 25:
        prediction = model_old.predict(df)
    
    return prediction
        
    

   

        
        
    










