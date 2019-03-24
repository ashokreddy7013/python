print("Login Validation")
uemail = input("Enter Email id : ")
upass = input("Enter Password : ")

from pymongo import MongoClient
db = MongoClient("localhost:27017").Employee_details
result = db.Employee.find({"email":uemail,"password":upass})

for x in result:
    print("Welcome Mr/Miss : ",x["name"])
    print(x["cno"])