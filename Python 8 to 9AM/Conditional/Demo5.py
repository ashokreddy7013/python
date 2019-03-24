
def createTable():
    import sqlite3 as sql
    conn = sql.connect("ICICI.db")
    curs = conn.cursor()
    curs.execute("create table account_info(acno number,pin number,name text,balance real)")
    conn.close()

def insertData():
    acno = int(input("Acno :"))
    pin = int(input("Pin :"))
    name = input("Name :")
    balane = float(input("Balance :"))
    import sqlite3 as sql
    conn = sql.connect("ICICI.db")
    curs = conn.cursor()
    curs.execute("insert into account_info values(?,?,?,?)",(acno,pin,name,balane))
    conn.commit()
    conn.close()

createTable()
insertData()
insertData()
insertData()
insertData()