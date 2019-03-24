

email = input(" Email ID : ")

from pymongo import MongoClient
db = MongoClient("localhost:27017").Employee_details
result = db.Employee.find({"email":email})

for x in result:
    print(x["name"])
    print(x["cno"])
    print(x["email"])
    print(x["password"])