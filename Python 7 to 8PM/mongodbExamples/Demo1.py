
from pymongo import MongoClient
mc = MongoClient("localhost",27018)
db = mc.sathya # Creating DB
print(db)
coll = db.employee # Creating a collection
print(coll)
d1={"idno":101,"name":"Ravi","salary":125000.00}
coll.insert(d1)
print("Data Inserted")

