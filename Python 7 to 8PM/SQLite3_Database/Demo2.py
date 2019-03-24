
import sqlite3 as sql
conn = sql.connect("icici.db")
curs = conn.cursor()
curs.execute("create table account_info (acno number primary key,name text,balance real,status text)")
print("Table Created")
conn.close()
