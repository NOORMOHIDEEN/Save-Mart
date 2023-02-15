import streamlit as st
import pandas as pd  
def get_data_from_excel():
    df = pd.read_excel(
        io="supermarkt_sales.xlsx",
        engine="openpyxl",
        sheet_name="Sales",
        skiprows=0,
        usecols="B:R",
        nrows=1100,
    )    
    df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df
st.title("Currently Updated Data Of the Super Market:")
df = get_data_from_excel()
st.write(df.tail())