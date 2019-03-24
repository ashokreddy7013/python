sno = int(input("Enter SNO : "))
name = input("Enter Name : ")
marks = int(input("Enter Marks : "))
status = input("Enter Status : ")

import sqlite3 as sql
conn = sql.connect("sathya.db")
curs = conn.cursor()
curs.execute("insert into student_info values(?,?,?,?)",(sno,name,marks,status))
conn.commit()
conn.close()
print(sno," Data Inserted")






