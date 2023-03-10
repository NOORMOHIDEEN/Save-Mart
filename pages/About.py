import streamlit as st
import pandas as pd  
import numpy as np
import plotly.express as px  
new_title = '<p style="font-family:sans-serif; color:#5499C7;  font-size: 35px;">Save Mart</p>'
st.markdown(new_title, unsafe_allow_html=True)
new_title = '<p style="font-family:sans-serif; color:#5499C7;  font-size: 20px;">The Location Of the Save Mart SuperMarket In San Fransico Are:</p>'
st.markdown(new_title, unsafe_allow_html=True)
def get_data_from_excel():
    df = pd.read_excel(
        io="supermarkt_sales.xlsx",
        engine="openpyxl",
        sheet_name="Sales",
        skiprows=0,
        usecols="B:R",
        nrows=1000,
    )    
    df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df

df = get_data_from_excel()
hide_style="""
        <style>
        #MainMenu {visibility:hidden;}
        header{visibility:hidden;}
        footer{visibility:hidden;}
        </style>
        """   
st.markdown(hide_style,unsafe_allow_html=True)
df1 = pd.DataFrame(
    np.random.randn(15, 2) / [50, 50] + [37.74, -122.42],
    columns=['lat', 'lon'])

st.map(df1)