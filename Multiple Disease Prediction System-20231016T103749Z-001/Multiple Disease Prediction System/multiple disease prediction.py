# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 00:04:31 2023

@author: Shubham Ramjanak Maurya
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('E:/My Projects/Multiple Disease Prediction System/Saved models/diabetes_trained_model.sav','rb'))

heart_disease_model = pickle.load(open('E:/My Projects/Multiple Disease Prediction System/Saved models/heart_trained_model.sav','rb'))

parkinsons_model = pickle.load(open('E:/My Projects/Multiple Disease Prediction System/Saved models/parkisons_trained_model.sav','rb'))

# create the side bar for navigation

with st.sidebar: 
    
    selected = option_menu('Multiple Disease      Prediction System',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           
                           icons = ['activity','heart-pulse','person-add'],
                           default_index = 0)
    
    
    
# 1) Diabetes Predicition Page
if (selected == 'Diabetes Prediction'):
    
    st.markdown(
        """
        <style>
        body {
            background-image: url('E:/My Projects/Multiple Disease Prediction System/img1.jpg');
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # page title
    st.title('Diabetes Prediction Using ML')
    
    
    
    # getting the input data from user
    # columns forinput fields
    col1, col2, = st.columns(2)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col1:
        BloodPressure = st.text_input('BloodPressure Value')
        
    with col2:
         SkinThickness = st.text_input('Skin Thickness Value')
         
    with col1:
         Insulin = st.text_input('Insulin Level')
         
    with col2:
           BMI = st.text_input('BMI Value')
           
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
        
    with col2:
        Age = st.text_input('Age of the Person')
        
        
     # Display a message using st.markdown()
    st.markdown("Fill in the necessary details then click on Diabetes test result")
  
    
#Code for Prediction
diab_diagnosis = ''


# Creating a button for prediction 

if st.button('Diabetes Test Result'):
        # Convert input variables to numeric types
        Pregnancies = int(Pregnancies)
        Glucose = float(Glucose)
        BloodPressure = float(BloodPressure)
        SkinThickness = float(SkinThickness)
        Insulin = float(Insulin)
        BMI = float(BMI)
        DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
        Age = int(Age)

        # Perform prediction
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The Person is Diabetic'
            st.error(diab_diagnosis)
        else:
            diab_diagnosis = 'The Person is Not Diabetic'
            st.success(diab_diagnosis)
 
    
    
# 2) Heart Disease Predicition Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction Using ML')
    
    # getting the input data from user
    # columns forinput fields

    age = st.text_input('Age of the Person')
    sex = st.text_input('Gender of Person (1 = male & 0 = female)')
    cp = st.text_input('Enter the Chest Pain Type')
    trestbps = st.text_input('Enter the Trestbps - Resting Blood Pressure (in mm Hg on Admission to the Hospital)')
    chol = st.text_input('Enter the Serum Cholestoral in mg/dl')
    fbs = st.text_input('Enter the Fasting Blood Sugar & gt; 120 mg/dl (1 = true; 0 = false)')
    restecg = st.text_input('Enter the Resting Electrocardiographic Results')
    thalach = st.text_input('Enter the Maximum Heart Rate Achieved')
    exang = st.text_input('Enter the Eexercise Induced Angina (1 = yes and 0 = no)')
    oldpeak = st.text_input('Enter the ST Depression Induced by Exercise Relative to Rest)')
    slope = st.text_input('Enter The Slope of the Peak Exercise ST Segment')
    ca = st.text_input('Enter the Number of Major Vessels (0-3) Colored by Flourosopy')
    thal = st.text_input('Enter the Thalassemia: 0 = Normal; 1 = Fixed defect; 2 = Reversable defect')
    
    # Display a message using st.markdown()
    st.markdown("Fill in the necessary details and click on Heart Disease test result")
    
    
#Code for Prediction
heart_diagnosis = ''

# Creating a button for prediction

if st.button('Heart Disease Test Result'):
        # Convert input variables to numeric types
        age = int(age)
        sex = int(sex)
        cp = int(cp)
        trestbps = float(trestbps)
        chol = float(chol)
        fbs = int(fbs)
        restecg = int(restecg)
        thalach = float(thalach)
        exang = int(exang)
        oldpeak = float(oldpeak)
        slope = int(slope)
        ca = int(ca)
        thal = int(thal)

        # Perform prediction
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        if heart_prediction[0] == 0:
            heart_diagnosis = 'The Person does not have Heart Disease'
            st.success(heart_diagnosis)
        else:
            heart_diagnosis = 'The Person has Heart Disease'
            st.error(heart_diagnosis)



# 3) Parkinsons Predicition Page
if (selected == 'Parkinsons Prediction'):
    
    # page title
    st.title('Parkinsons Prediction Using ML')
    
    # getting the input data from user
    
    MDVP_Fo = st.text_input('MDVP Fo (Hz) - Average vocal fundamental frequency')
    MDVP_Fhi = st.text_input('MDVP Fhi (Hz) - Maximum vocal fundamental frequency')
    MDVP_Flo = st.text_input('MDVP Flo (Hz) - Minimum vocal fundamental frequency')
    MDVP_Jitter_percent = st.text_input('MDVP Jitter (%) - Several measures of variation in fundamental frequency')
    MDVP_Jitter_Abs = st.text_input('MDVP Jitter Abs - Several measures of variation in fundamental frequency')
    MDVP_RAP = st.text_input('MDVP RAP - Several measures of variation in fundamental frequency')
    MDVP_PPQ = st.text_input('MDVP PPQ - Several measures of variation in fundamental frequency')
    Jitter_DDP = st.text_input('Jitter DDP - Several measures of variation in fundamental frequency')
    MDVP_Shimmer = st.text_input('MDVP Shimmer - Several measures of variation in fundamental frequency')
    MDVP_Shimmer_dB = st.text_input('MDVP Shimmer dB - ')
    Shimmer_APQ3 = st.text_input('Shimmer APQ3 - ')
    Shimmer_APQ5 = st.text_input('Shimmer APQ5 - ')
    MDVP_APQ = st.text_input('MDVP APQ - ')
    Shimmer_DDA = st.text_input('Shimmer DDA - ')
    NHR = st.text_input('NHR - Measures of ratio of noise to tonal components in the voice')
    HNR = st.text_input('HNR - Measures of ratio of noise to tonal components in the voice')
    RPDE = st.text_input('RPDE - Nonlinear dynamical complexity measures')
    DFA = st.text_input('DFA - Signal fractal scaling exponent')
    spread1 = st.text_input('Spread1 - Nonlinear measures of fundamental frequency variation')
    spread2 = st.text_input('Spread2 - Nonlinear measures of fundamental frequency variation')
    D2 = st.text_input('D2 - Nonlinear dynamical complexity measures')
    PPE = st.text_input('PPE - Nonlinear measures of fundamental frequency variation')
    
    # Display a message using st.markdown()
    st.markdown("Fill in the necessary details and click on Parkinsons test result")

    
#Code for Prediction
Parkinsons_diagnosis = ''


# Creating a button for prediction
if st.button('Parkinsons Test Result'):
        # Convert input variables to appropriate types
        MDVP_Fo = float(MDVP_Fo)
        MDVP_Fhi = float(MDVP_Fhi)
        MDVP_Flo = float(MDVP_Flo)
        MDVP_Jitter_percent = float(MDVP_Jitter_percent)
        MDVP_Jitter_Abs = float(MDVP_Jitter_Abs)
        MDVP_RAP = float(MDVP_RAP)
        MDVP_PPQ = float(MDVP_PPQ)
        Jitter_DDP = float(Jitter_DDP)
        MDVP_Shimmer = float(MDVP_Shimmer)
        MDVP_Shimmer_dB = float(MDVP_Shimmer_dB)
        Shimmer_APQ3 = float(Shimmer_APQ3)
        Shimmer_APQ5 = float(Shimmer_APQ5)
        MDVP_APQ = float(MDVP_APQ)
        Shimmer_DDA = float(Shimmer_DDA)
        NHR = float(NHR)
        HNR = float(HNR)
        RPDE = float(RPDE)
        DFA = float(DFA)
        spread1 = float(spread1)
        spread2 = float(spread2)
        D2 = float(D2)
        PPE = float(PPE)
        
        
        # Perform prediction
        parkinsons_prediction = parkinsons_model.predict([[MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter_percent, MDVP_Jitter_Abs,
                                                           MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer,
                                                           MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5,
                                                           MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1,
                                                           spread2, D2, PPE]])
        if parkinsons_prediction[0] == 0:
            Parkinsons_diagnosis = "The Person does not have Parkinsons Disease"
            st.success(Parkinsons_diagnosis)
        else:
            Parkinsons_diagnosis = "The Person has Parkinsons"
            st.error(Parkinsons_diagnosis)






# Display a message at the end using st.markdown()
st.markdown('Shubham Maurya(54) and Prince Mishra(58)')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    