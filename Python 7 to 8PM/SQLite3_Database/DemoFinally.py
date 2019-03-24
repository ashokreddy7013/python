
acno = int(input("Account No : "))
name = input("Name : ")
amount = float(input("Amount : "))
status = input("Status : ")

import sqlite3 as sql
conn = sql.connect("icici.db")
curs = conn.cursor()
t1 = (acno,name,amount,status)
try:
    curs.execute("insert into account_info values (?,?,?,?)",t1)
except sql.IntegrityError:
    print("Invalid Account No")
else:
    conn.commit()
    print(acno," is Created")
finally:
    conn.close()
    print("Thanks")
