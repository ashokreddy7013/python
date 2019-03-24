
# reading all marks and names

import sqlite3 as sql
conn = sql.connect("sathya.db")
curs = conn.cursor()
curs.execute("Select marks,name from student_info")
result = curs.fetchall()
print(result)