
s1 = {10,20,30,40,50}
print(s1)
s1.add(90)
print(s1)
s2 = s1.copy()
print(s2)
s2.clear()
print(s2) # set()
print("-------------------")

s1 = {10,20,30,40}
s2 = {30,40,50,60}
s3 = s1.difference(s2)
print(s3)
s3 = s2.difference(s1)
print(s3)
print("---------------------")

s1 = {10,20,30,40}
s2 = {30,40,50,60}
s3 = s1.intersection(s2)
print(s3)
print("---------------------")

s1 = {10,20,30,40}
s2 = {30,40,50,60}
result = s1.issubset(s2)
print(result)

print("---------------------")

s1 = {10,20,30,40}
s2 = {30,40,50,60}
result = s1.issuperset(s2)
print(result)

print("-------------------------")
s1 = {10,20,30,40,50}
print(s1)
no = s1.pop()
print(s1)
print("Removed No ",no)

print("-------------------------")
s1 = {10,20,30,40,50}
print(s1)
s1.remove(30)
print(s1)
print("---------------------")

s1 = {10,20,30,40}
s2 = {30,40,50,60}
s3 = s1.union(s2)
print(s3)

print("---------------------")

s1 = {10,20,30,40}
s2 = {30,40,50,60}
s1.update(s2)
print(s1)
print(s2)