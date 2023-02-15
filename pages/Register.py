import streamlit as st
import datetime
import pandas as pd  
from openpyxl import load_workbook
st.title("Register the Supermarket Details :")
with st.form(key='my_form'):
    id=st.text_input("Invoice ID","750-67-8428")
    branch=st.text_input("Branch",'A')
    city=st.text_input("City","Yangon")
    type=st.radio("Customer_type",("Member","Normal"))
    gender=st.radio("Gender",("Male","Female"))
    product_line=st.selectbox("Product Line",(
        'Please Select a Type','Health and beauty','Electronic accessories','Home and lifestyle',
        'Sports and travel','Food and beverages','Fashion accessories'
    ))
    unit_price=st.number_input("Unit Price",74.69)
    quantity=st.number_input("Quantity",7)
    tax=st.number_input("Tax",5.10)
    total=st.number_input("Total",500.00)
    date=st.date_input("Date",datetime.date(2023,2,2))
    time=st.time_input("Time",datetime.time(8,15))
    payment=st.radio("Payment",("Ewallet","Cash","Credit Card"))
    cogs=st.number_input("Cogs",76.40)
    gmp=st.number_input("Gross Margin in %",4.761904762)
    gi=st.number_input("Gross Income",10.00)
    rating=st.number_input("Rating",9.10)
    submit = st.form_submit_button(label='Submit')

if submit:
    st.markdown('<p class="submit" style="color:#36E110;text-align: center;">Successfully Submitted</p>',unsafe_allow_html=True)
    rows = [[id, branch, city,type,gender,product_line,unit_price,quantity,tax,total,date,time,payment,cogs,gmp,gi,rating]]
    df=pd.DataFrame(rows)    
    st.write(df)
    workbook_name = 'supermarkt_sales.xlsx'
    wb = load_workbook(workbook_name)
    page = wb.active    
    for info in rows:
        page.append(info)
    wb.save(filename=workbook_name)




