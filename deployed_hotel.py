import numpy as np
import pandas as pd
import streamlit as st
import joblib  
# Lets load all the instanced required over here
with open('transformer_joblib','rb') as file:
    transformer = joblib.load(file)
# Lets load the model
with open('final_model.joblib','rb') as file:
    model = joblib.load(file)
st.title("INN Hotel Group")
st.header(":orange[Hotel Booking Cancellation Prediction]")

# Let's take input from the user

amnth = st.slider("Arrival Month",min_value=1,max_value=12,step=1)
wkd_lambda = (lambda x:0 if x == 'M' else 
              1 if x == 'T' else
              2 if x == 'W' else
              3 if x == 'Th' else
              4 if x == 'F' else
              5 if x == 'Sa' else 6)
awkd = wkd_lambda(st.selectbox("Arrival Weekday",['M','T','W','Th','F','Sa','Su']))
dwkd = wkd_lambda(st.selectbox("Departure Weekday",['M','T','W','Th','F','Sa','Su']))
wkend = st.number_input("Weekend Nights",min_value=0)
wk = st.number_input("Week Nights",min_value=0)
tot_nights = wk + wkend
mkt = (lambda x:0 if x ==  'offline' else 1)(st.selectbox("Market Segment",['offline','online']))
lt = st.number_input("Lead Time (days prior booking)",min_value=0)
price = st.number_input("Average Price per Night",min_value=100)
adul = st.number_input("Number of Adults",min_value=1,max_value=5)
spcl = st.selectbox("Special Requests",[0,1,2,3 ])
park = (lambda x:0 if x == 'No' else 1)(st.selectbox("Parking Required",['No','Yes']))
# transform the data
lt_t,price_t = transformer.transform([[lt,price]])[0]
input_list = [lt_t,spcl,price_t,adul,wkend,park,wk,mkt,amnth,awkd,tot_nights,dwkd]
# make prediction
prediction = model.predict_proba([input_list])[:,1][0]
# lets show the probability
if st.button('predict'):
    st.success(f'The probability of cancellation is {prediction:.2f}')