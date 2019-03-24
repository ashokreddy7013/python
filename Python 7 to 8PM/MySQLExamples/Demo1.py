
import mysql.connector as my
conn = my.connect(user="root",password="",host="127.0.0.1",port="3306",database="sathya")
# conn = my.connect(user="root",password="",host="127.0.0.1",
#                   port="3306",database="sathya")

def TableCreation():
    curs = conn.cursor()
    curs.execute("create table if not exists employee(idno integer(4) primary key,name varchar(50),salary integer(10))")
    print("Table Created")

def datainsert(idno,name=None,salary=0.0):
    curs = conn.cursor()
    curs.execute("insert into employee values (%s,%s,%s)",(idno,name,salary))
    conn.commit()
    print("Employee Inserted")

def readAll():
    curs = conn.cursor()
    curs.execute("select * from employee")
    result = curs.fetchall()
    for x in result:
        print(x)

def readEmployee(idno):
    curs = conn.cursor()
    curs.execute("select * from employee where idno = %s",(idno,))
    result = curs.fetchone()
    print(result)

def deleteEmployee(idno):
    curs = conn.cursor()
    curs.execute("delete from employee where idno = %s",(idno,))
    conn.commit()
    print(idno," Employee Deleted")

if __name__ == '__main__':
    TableCreation()
    while True:
        print("1) Insert ")
        print("2) View All Employees ")
        print("3) View 1 Employee ")
        print("4) Delete ")
        print("5) Exit ")
        option = int(input("Select One Option : "))
        if option == 1:
            try:
                idno = int(input("Idno : "))
                name = input("Name : ")
                salary = int(input("Salary : "))
                datainsert(idno,name,salary)
            except:
                print("Invalid Input")
        elif option == 2:
            readAll()
        elif option == 3:
            idno = int(input("Idno : "))
            readEmployee(idno)
        elif option == 4:
            idno = int(input("Idno : "))
            deleteEmployee(idno)
        elif option == 5:
            break
            conn.close()
        else:
            print("Invalid Option")

        ans = input("To Continue type Yes:")
        if ans.lower().strip() == "yes":
            continue
        else:
            break
            conn.close()
    print("Thanks")