
# Set Class Methods
# ===================
s1 = {10,20,30,40,50}
print(s1)
s1.add(60)
print(s1)
print("-------------------")
s2 = s1.copy();
print(s1)
print(id(s1))
print(s2)
print(id(s2))
# Modification of s1 and s2
s1.add(500)
s2.add(1000)
print(s1)
print(s2)
print("-------------------")

s1 = {10,20,30,40}
s2 = {30,40,50,60}
s3 = s1.difference(s2)
print(s3)
s4 = s2.difference(s1)
print(s4)
print("-------------------")

s1 = {10,20,30,40}
s2 = {30,40,50,60}
s3 = s1.intersection(s2)
print(s3)
print("-------------------")

s1 = {10,20,30,40}
s2 = {30,40,50,60}
result = s1.issubset(s2)
print(result)

print("-------------------")

s1 = {10,20,30,40}
s2 = {30,40,10,20}
result = s1.issubset(s2)
print(result)
print("-------------------")

s1 = {10,20,30,40}
print(s1)
s1.pop()
print(s1)
print("-------------------")

s1 = {10,20,30,40}
s1.remove(20)
print(s1)
print("-------------------")

s1 = {10,20,30,40}
s2 = {30,40,10,20}
s3 = s1.union(s2)
print(s3)

print("-------------------")

s1 = {10,20,30,40,60}
s2 = {30,40,10,20,50}
s1.update(s2)
print(s1)
print(s2)