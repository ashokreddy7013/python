d1 = {101:"Ravi",102:"Kumar",103:"Krishna"}
print(d1)
d2 = d1.copy()
print(d2)
value = d2.get(103)
print(value)
value = d2.get(104)
print(value)
print("-----------------")
it = d2.items()
print(it)
print(type(it))

print("-----------------")
it = d2.keys()
print(it)
print(type(it))

print("-----------------")
it = d2.values()
print(it)
print(type(it))

print("-----------------")
print(d2)
value = d2.pop(102)
print(value)
print(d2)

print("-----------------")
print(d2)
d2.popitem()
print(d2)

print("-----------------")
d1 = {101:"Ravi",102:"Kumar",103:"Krishna"}
print(d1)
value = d1.setdefault(101)
print(value)
value = d1.setdefault(105)
print(value)
print(d1)
