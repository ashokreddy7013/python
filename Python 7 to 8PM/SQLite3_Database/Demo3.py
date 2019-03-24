
# Example to insert data into account_info

import sqlite3 as sql
conn = sql.connect("ICICI.db")
curs = conn.cursor()
curs.execute("insert into account_info values (101,'Ravi',1025000,'active')")
print("Data inserted")
conn.commit()
conn.close()
