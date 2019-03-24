
acno = int(input("Account No : "))
import sqlite3 as sql
conn = sql.connect("icici.db")
curs = conn.cursor()
curs.execute("delete from account_info where acno = ?",(acno,))
conn.commit()
conn.close()
print(acno,"is Deleted")