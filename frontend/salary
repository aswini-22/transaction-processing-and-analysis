import streamlit as st
import pandas as pd
import mysql.connector

# ------------------- Connect to MySQL -------------------
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",   # Put your MySQL password here
    database="salary_management"
)

# Cursor for executing SQL queries
cursor = mydb.cursor()

# ------------------- Streamlit UI -------------------
st.title("Salary & Expenses Management System")

st.subheader("Add a New Expense")

# Input fields
category = st.text_input("Category")
amount = st.number_input("Amount", min_value=0.0, step=0.01)

# Button to add expense
if st.button("Add Expense"):
    if category and amount > 0:
        query = "INSERT INTO expenses (category, amount) VALUES (%s, %s)"
        cursor.execute(query, (category, amount))
        mydb.commit()
        st.success(f"Added expense: {category} - {amount}")
    else:
        st.error("Please enter valid category and amount!")

# ------------------- Display Expenses Table -------------------
st.subheader("All Expenses")
df = pd.read_sql("SELECT * FROM expenses", mydb)
st.dataframe(df)

# ------------------- Plot Expenses -------------------
st.subheader("Expenses Chart")
if not df.empty:
    chart = pd.DataFrame(df.groupby("category")["amount"].sum()).reset_index()
    st.bar_chart(chart.set_index("category"))
else:
    st.write("No expenses to show yet.")
