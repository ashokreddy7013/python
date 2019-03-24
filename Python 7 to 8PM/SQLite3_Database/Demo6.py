

acno = int(input("Enter Account No : "))
import sqlite3 as sql
conn = sql.connect("icici.db")
curs = conn.cursor()
curs.execute("select * from account_info where acno = ?",(acno,))
result = curs.fetchone()
if result == None:
    print("Invalid Account No")
else:
    print(result)
    print(type(result))
