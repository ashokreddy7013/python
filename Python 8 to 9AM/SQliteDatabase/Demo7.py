
import sqlite3 as sql
conn = sql.connect("sathya.db")
curs = conn.cursor()
sno = int(input("Enter SNO : "))
curs.execute("delete from student_info where sno = ?",(sno,))
conn.commit()
conn.close()
print(sno," is Deleted")