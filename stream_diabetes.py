import pickle
import streamlit as st

# Load Model
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))



#judul Web
st.title('Data Mining Prediksi Diabetes')

Pregnancies = st.text_input ('input nilai Pregnancies')

Glucose = st.text_input('input nilai Glucose')

BloodPressure = st.text_input ('input nilai Blood Pressure')

SkinThickness = st.text_input ('input nilai Skin Thickness')

Insulin = st.text_input ('input nilai Insulin')

BMI = st.text_input ('input nilai BMI')

DiabetesPedigreeFunction = st.text_input ('input nilai Diabetes Pedigree Function')

Age = st.text_input ('input nilai Age')

#Code untuk Prediksi

diab_diagnosis = ''

#Button Prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
    if(diab_prediction[0] == 0):
        diab_diagnosis = 'Tidak Diabetes'
    else :
        diab_diagnosis = 'Diabetes'
    
    st.success(diab_diagnosis)



