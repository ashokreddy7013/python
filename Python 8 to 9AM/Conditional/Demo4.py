 # WAP for ATM Process
 # The Process must Contain
 # 1. Withdraw
 # 2. Deposit
 # 3. Balance Check

import sqlite3 as sql
conn =sql.connect("ICICI.db")
curs = conn.cursor()

uacno = int(input("Enter Account No : "))
upin = int(input("Enter Pin No : "))
curs.execute("select name,balance from account_info where acno = ? and pin = ?",(uacno,upin))
res = curs.fetchone()
if res == None:
    print("Invalid Details")
else:
    print("Welcome Mr/Miss : ",res[0])
    print("Available Balance :",res[1])
    print("1) Deposit")
    print("2) Withdraw")
    print("3) Balance Check")
    option = int(input("Select One Option :"))
    if option == 1:
        amount = float(input("Enter Amount to Deposit : "))
        total = amount + res[1]
        curs.execute("update account_info set balance = ? where acno = ?",(total,uacno))
        conn.commit();
        print("Amount Deposited")
    elif option == 2:
        amount = float(input("Enter Amount to Withdraw :"))
        if res[1] >= amount:
            total = res[1]-amount
            curs.execute("update account_info set balance = ? where acno = ?",(total,uacno))
            conn.commit()
            print("Withdrawl is Done")
        else:
            print("No Fund's")
    elif option == 3:
        print("Available Balance :", res[1])
    else:
        print("Please Select From Given Options Only")
print("Thanks")
print("Visit Again")