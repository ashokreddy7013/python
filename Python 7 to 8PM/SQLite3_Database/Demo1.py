
# Example program to Create database
# and get Connection

import sqlite3 as sql
#conn = sql.connect("ICICI.db")
conn = sql.connect(r"C:\Users\android\Desktop\ICICI.db")
print("My DB Connection ",conn)
conn.close()# Closing Connection