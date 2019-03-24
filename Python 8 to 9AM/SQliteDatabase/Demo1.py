
import sqlite3 as sql
conn = sql.connect("sathya.db")
curs = conn.cursor()
curs.execute("create table student_info(sno number,name text,marks number,status text)")
conn.close()
print("Table Created")