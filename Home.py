import streamlit as st
import pandas as pd
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



def main():    
    st.title("SuperMarket Data Analysis And Register Data ")
    
    df = get_data_from_excel()
    st.subheader("Data which needed to be Entered:")
    col1, col2 = st.columns(2)
    list_of_column_names = []
    
    for row in df:       
            list_of_column_names.append(row) 
    with col1:
        for i in range(0, 9):                
            st.write("---> "+list_of_column_names[i])
            
    with col2:
        for i in range(9, 17):                
            st.write("---> "+list_of_column_names[i])
        
            
    st.header("Data Which are entered in the DataBase Are:")
    st.write(df)
    
if __name__ == '__main__':
    main()