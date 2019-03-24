
import sqlite3 as sql
conn = sql.connect("icici.db")
curs = conn.cursor()
curs.execute("select * from account_info")
result = curs.fetchall()
print(result)
print(type(result))

