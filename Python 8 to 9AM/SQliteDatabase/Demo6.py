
import sqlite3 as sql
conn = sql.connect("sathya.db")
curs = conn.cursor()
sno = int(input("Enter SNO : "))
curs.execute("select * from student_info where sno = ?",(sno,))
result = curs.fetchone()
print(result)
conn.close()