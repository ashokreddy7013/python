import re
s1 = "Hello this is sathya Contact"
result = re.findall(r"^\w+",s1)
print(result)

print("------------------")

s1 = "Hello this is sathya Contact"
result = re.findall(r"\w+$",s1)
print(result)

print("------------------")

s2 = "sathya is a python"
res1 = re.findall(r"^\w+",s2)
res2 = re.findall(r"\w+$",s2)
print(res1,res2)
if res1[0] == "sathya" and res2[0] == "sathya":
    print("valid")
else:
    print("Invalid")

print("------------------")

s1 = "This is naveen from sathya tech"
result = re.findall(r"^\w+$",s1)
print(result)
