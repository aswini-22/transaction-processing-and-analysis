import streamlit as st
import pandas as pd
from database.db_connection import get_connection

# Connect to DB
mydb = get_connection()
cursor = mydb.cursor()

st.header("Add Expense")

category = st.text_input("Category")
amount = st.number_input("Amount", min_value=0.0, step=0.01)

if st.button("Add Expense"):
    if category and amount > 0:
        query = "INSERT INTO expenses (category, amount) VALUES (%s, %s)"
        cursor.execute(query, (category, amount))
        mydb.commit()
        st.success("Expense Added Successfully!")
    else:
        st.error("Enter valid data!")

st.subheader("All Expenses")

df = pd.read_sql("SELECT * FROM expenses", mydb)
st.dataframe(df)
