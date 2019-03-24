accno = int(input("Account No : "))
name = input("Name : ")
amount = float(input("Amount to Deposit : "))
status = input("Status : ")

import sqlite3 as sql
conn = sql.connect("icici.db")
curs = conn.cursor()
try:
    curs.execute("insert into account_info values (?,?,?,?)",(accno,name,amount,status))
    conn.commit()
except sql.IntegrityError as ie:
    print("Account No is Available")
else:
    print(accno ,"is Created")
finally:
    conn.close()


