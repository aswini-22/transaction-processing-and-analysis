import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",        # blank if no password in XAMPP
    database="salary_management"
)

print("✅ Connected to MySQL!")
