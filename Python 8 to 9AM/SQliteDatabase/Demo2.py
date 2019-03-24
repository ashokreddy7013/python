# Insert the data
import sqlite3 as sql
conn = sql.connect("sathya.db")
curs = conn.cursor()
curs.execute("insert into student_info values(101,'Ravi',350,'Pass')")
conn.commit()# Save
conn.close()
print("Data Inserted")
