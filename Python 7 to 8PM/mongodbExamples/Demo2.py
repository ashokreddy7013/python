
name = input("Name : ")
contact = int(input("Contact No : "))
email = input("Email Id : ")
password = input("Password : ")

emp_details = {"name":name,"cno":contact,"email":email,"password":password}

from pymongo import MongoClient
# mc = MongoClient("localhost:27017")
# db = mc.Employee_details # Creating DB
# coll = db.Employee # Creating Collection
# coll.insert(emp_details)
# print("Employee Inserted")

MongoClient("localhost:27017").Employee_details.Employee.insert(emp_details)
print("Employee Inserted")