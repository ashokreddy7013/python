
import  re
name = input("Enter Name (must be in small): ")
res = re.match(r"^[a-z]*$",name)
if res == None:
    print("Invalid Name")
else:
    print("Valid Name")

print("------------------------")

name = input("Enter Name : ")
res = re.match(r"^[A-Za-z]*$",name)
if res == None:
    print("Invalid Name")
else:
    print("Valid Name")