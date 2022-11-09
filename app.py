import streamlit as st
import numpy as np
import string
import pickle
st.set_option('deprecatiion.showfileUploaderEncoding',False)
model=pickle.load(open('insurance.pkl',rb))

def main():
    st.sidebar.header("Insurance Cost Prediction")
    st.sidebar.text("This is a Web App that tells you the predicted insurance cost.")
    st.sidebar.header("just fill in your information below")
    st.sidebar.text("The AdaBoost REgressmodel was used")

    age=st.slidebar("Age",0,100)
    sex=st.radio("Gender",("Male","Female","Trangender"))
    bmi=st.slidebar("Your BMI",0.0,70.0)
    children=st.slidebar("How many children ?",0,10)
    smoker= st.radio("Are You a Smoker?",('Yes','No'))
    region=st.radio("Your Region",('southwest','southeast','northwest','northeast'))
   
    inputs=[[age,sex,bmi,children,smoker,region]]

    if st.button('Predict'):
        result=model.predict(inputs)
        updated_result=result.flatten().astype(float)
        st.sucess("Your Insurance Cost will be{}.".format(updated_result))

if __name__ =='_main_'  :
    main()
