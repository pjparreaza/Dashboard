import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


def load_data():
    url= 'coffee_ratings.csv'
    df = pd.read_csv(url)
    df_interin = df.copy()
    df_interin = df_interin[['total_cup_points',
                             'species',
                             'country_of_origin',
                             'variety',
                             'aftertaste',
                             'acidity',
                             'aroma',
                             'body',
                             'balance',
                             'sweetness',
                             'altitude_mean_meters',
                             'moisture']]

    
    
    df_interin = df_interin.dropna()
    df_interin['species'] = pd.Categorical(df_interin['species'])
    df_interin['country_of_origin'] = pd.Categorical(df_interin['country_of_origin'])
    df_interin['variety'] = pd.Categorical(df_interin['variety'])
    df_interin['speciality'] = df_interin['total_cup_points'].apply(lambda x: 'yes' if x>82.43 else 'no')
    df_interin['speciality'] = pd.Categorical(df_interin['speciality'])
    df = df_interin.copy()
    return df

df_ch =load_data()
st.write(df_ch.shape[0])  ## Para traer las filas


st.title('Coffe Dashboard')
st.dataframe(df_ch)
#st.write(x, 'squared is', x * x)
#y = st.slider('Select another value:', min_value = -5,max_value=5,value=0)
#st.write(y, 'Cubit is', y**3)

# cargar csv

fig1 = px.histogram(df_ch,x='aroma')
st.plotly_chart(fig1)

fig2 = sns.pairplot(data=df_ch.select_dtypes('number'), hue ='speciality')
st.pyplot(fig2)