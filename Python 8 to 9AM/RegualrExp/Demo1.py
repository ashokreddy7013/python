import re
s1 = "This is Naveen from sathya, Naveen"
result = re.match("Naveen",s1)
print(result)
print("------------------")
result = re.search("Naveen",s1)
print(result)