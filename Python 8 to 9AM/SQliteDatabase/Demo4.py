

import sqlite3 as sql
conn = sql.connect("sathya.db")
curs = conn.cursor()
curs.execute("select * from student_info")
result = curs.fetchall()
print(result)






