import numpy as np
import pandas as pd
import streamlit as st
import joblib

# Lets load all the instances required over here
with open('transformer.joblib','rb') as file:
    transformer = joblib.load(file)


# Lets load the model

with open(f'Final_model.joblib','rb') as file:
    model = joblib.load(file)


st.title('INN HOTEL GROUP')
st.header(' This application will predict the chancs of the booking cancellation')

# Lets Take the input from the user

amnth = st.slider('Select Your month or arrival',min_value=1,max_value=12,step=1)
wkd_lambda = (lambda x: 0 if x=='Mon' else
              1 if x=='Tue' else
              2 if x=='Wed' else
              3 if x=='Thru' else
              4 if x=='Fri' else
              5 if x=='Sat' else 6)
awkd = st.selectbox('Select Your Weekday of arrival',['Mon','Tue','Wed','Thru','Fri','Sat','Sun'])
dwkd = awkd = wkd_lambda(st.selectbox('Select Your Day of departure',['Mon','Tue','Wed','Thru','Fri','Sat','Sun']))
wkend = st.number_input('Enter How many weekend night are there in stay',min_value=0)
wk = st.number_input('Enter How many week night are there in stay',min_value=0)
totn = wkend + wk
mkt = (lambda x: 0 if x=='Offline' else 1)(st.selectbox('How the booking has been made?',['Offline','Online']))
lt = st.number_input('How many day prior the booking was made',min_value=0)
price = st.number_input('What is the average price per room',min_value=0)
adults = st.number_input('How many adult members in booking',min_value=0)
spcl = st.selectbox('Select the number of special request made',[0,1,2,3,4,5])
park = (lambda x: 0 if x=='N0' else 1)(st.selectbox('Does guest need the parking space',['Yes','N0']))

# Transform the data

lt_t,price_t = transformer.transform([[lt,price]])[0]

# Lets create the input list

input_list = [lt_t,spcl,price_t,adults,wkend,park,wk,mkt,amnth,wk,totn,dwkd]

# Make prediction
prediction = model.predict_proba([input_list])[:,1][0]

# lets show the probability
if st.button('Predict'):
    st.success(f'Cancellation chances: {(round(prediction,4))*100}%')