import sqlite3 as sql
conn = sql.connect("icici.db")
curs = conn.cursor()

def main():
    print("Welcome To MyBank")
    print(" 1) New Account")
    print(" 2) Login")
    option = int(input("Select One Option : "))
    if option == 1:
        print("New Account Process")
        registration()
    elif option == 2:
        print("Login Process")
        validation()
    else:
        print("Invalid Option")
    print("Thanks")

def validation():
    acno = int(input("Account No : "))
    pin = int(input("Pin No : "))
    curs.execute("select * from account_info where acno = ? and pin = ?",(acno,pin))
    res = curs.fetchone()
    if res == None:
        print("Invalid Details")
    else:
        print("Welcome Mr/Miss : ",res[2])
        print("Your Current Balance : ",res[3])
    print("1) Deposit")
    print("2) Withdraw")
    print("3) Exit")
    option = int(input("Select One Option : "))
    if option == 1:
        print("Deposit Process")
        amount = float(input("Enter Amount : "))
        balance = amount+res[3]
        curs.execute("update account_info set balance = ? where acno = ?",(balance,acno))
        conn.commit()
        print(amount," is Diposited")

    elif option == 2:
        print("Withdraw Process")
        amount = float(input("Withdrawl Amount : "))
        if amount%100 == 0:
            if amount<= 15000:
                if amount<= res[3]:
                    balance = res[3]-amount
                    curs.execute("UPDATE account_info set balance = ? where acno = ?",(balance,acno))
                    conn.commit()
                    print(amount," Is Withdrawl")
                else:
                    print("No Funds")
            else:
                print("Limit is 15000/- Only")
        else:
            print("Invalid Amount")

    elif option == 3:
        conn.close()
        exit()
    else:
        print("Invalid Option")

def acno_Autogen():
    curs.execute("create table if not exists account_info (acno number primary key ,pin number,name text,balance real,status text)")
    curs.execute("select max(acno) from account_info")
    res = curs.fetchone()
    if res[0] == None:
        auto_acno = 101
    else:
        auto_acno = res[0]
        auto_acno += 1

    return auto_acno

def registration():
    acno = acno_Autogen()
    print("Your Account No is : ",acno)
    pin = int(input("Pin No : "))
    name = input("Name : ")
    open_bal = float(input("Opening Balance : "))
    status = "active"
    curs.execute("insert into account_info values (?,?,?,?,?)",(acno,pin,name,open_bal,status))
    conn.commit()
    print(acno," is Created")

