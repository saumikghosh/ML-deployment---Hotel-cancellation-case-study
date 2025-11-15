import streamlit as st  
st.title("calculate bmi")
weight = st.text_input("enter weight in kg")
height = st.text_input("enter height in cm")
bmi = (int(weight)/(int(height)/100)**2)
if height ==0:
    bmi = 0
else:
    st.success(f"your bmi is {bmi} Kg/cm")