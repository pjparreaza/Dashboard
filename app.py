import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

#@st.cache
#def load_data():
#    url= 'coffee_rating.csv'
#    df = pd.read_csv(url)
#    df_interin = df.copy()
#    df_interin = df_interin[['']]

st.write('Hello world')
x = st.slider('Select a value:', min_value = -5,max_value=5,value=0)
st.write(x, 'squared is', x * x)
y = st.slider('Select another value:', min_value = -5,max_value=5,value=0)
st.write(y, 'Cubit is', y**3)

# cargar csv
