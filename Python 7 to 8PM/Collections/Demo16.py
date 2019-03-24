
d1 = {
    101:"Ravi",
    102:"Kumar",
    103:"Krishna",
    104:"Mohan",
    105:"Prasad"
    }
print(d1)
d2 = d1.copy()
print(d2)
print("----------------")
#emp_no = int(input("Enter Employee No : "))
#val = d1.get(emp_no)
#print(val)
print("----------------")
i = d1.items()
print(i)
print(type(i))
print("----------------")
k = d1.keys()
print(k)
print(type(k))
print("----------------")
v = d1.values()
print(v)
print(type(v))
print("----------------")
d1 = {
    101:"Ravi",
    102:"Kumar",
    103:"Krishna",
    104:"Mohan",
    105:"Prasad"
    }
key = int(input("Enter Idno : "))
val = d1.pop(key)
print("Removed Value is : ",val)
print(d1)


