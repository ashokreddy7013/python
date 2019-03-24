
t1 = (10,10.25,"Sathya")
print(t1)# (10,10.25,"Sathya")
print(type(t1)) # <class 'tuple'>

print("-------------------")
# packing
t2 = 20,30.25,"Ravi"
print(t2)
print(type(t2))

# un-packing
a,b,c = t2
print(a,type(a))
print(b,type(b))
print(c,type(c))

print("-------------------")
print(id(t2[1]))
print(id(b))