import streamlit as st
import pickle
import pandas as pd

pipe1 = pickle.load(open('pipe1.pkl', 'rb'))
pipe2 = pickle.load(open('pipe2.pkl', 'rb'))
pipe3 = pickle.load(open('pipe3.pkl', 'rb'))

castes = ['NT-D', 'NT-C', 'VJ-A', 'SBC', 'SC', 'Open', 'NT-B', 'ST', 'OBC', 'SEBC', 'EBC']

st.title("Admission Predictor")
given_marks = st.number_input('Mathematics Marks')
selected_caste = st.selectbox("Select Caste", castes)
input_df = pd.DataFrame({'marks': [given_marks], 'caste': [selected_caste]})
if st.button('Predict'):
    proba1 = pipe1.predict_proba(input_df)
    proba2 = pipe2.predict_proba(input_df)
    proba3 = pipe3.predict_proba(input_df)
    get_per1 = proba1[0][1]
    get_per2 = proba2[0][1]
    get_per3 = proba3[0][1]
    st.header('Chances for getting admission in 1st cut-off is {} %'.format(get_per1 * 100))
    st.header('Chances for getting admission in 1st cut-off is {} %'.format(get_per2 * 100))
    st.header('Chances for getting admission in 1st cut-off is {} %'.format(get_per3 * 100))
