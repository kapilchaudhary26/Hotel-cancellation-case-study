import streamlit as st

st.title('CALCULATE YOUR BMI')
wt = st.number_input('Enter your weight in KGs: ')
h = st.number_input('Enter your height in CMs: ')
if h==0:
    bmi=0
else:
    bmi = wt/h**2
st.success(f'Tour Bmi is {bmi} KG/M^2')

