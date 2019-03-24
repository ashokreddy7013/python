
s1 = "sathya"
s2 = s1.upper()
print(s2)
s3 = s2.lower()
print(s3)
print("---------------------")
s1 = "SathYa"
print(s1)
s2 = s1.swapcase()
print(s2)
print("---------------------")
s1 = "this is a sample string"
print(s1)
s2 = s1.title()
print(s2)
print("---------------------")
s1 = "this is a sample string"
print(s1)
s2 = s1.capitalize()
print(s2)
print("---------------------")
s1 = "  this is "
print(s1)
length = len(s1)
print(length)
s2 = s1.rstrip()
print(s2)
length = len(s2)
print(length)

s3 = s2.lstrip()
print(s3)
length = len(s3)
print(length)

print("---------------------")
s1 = "  this is "
print(s1)
print(len(s1))
s2 = s1.strip()
print(s2)
print(len(s2))

print("---------------------")
s1 = "Sathya"
print(s1)
s2 = s1.replace("S","i")
print(s2)

print("---------------------")
s1 = "ravi,kumar,krishna,mohan"
print(s1)
s2 = s1.split(",")
print(s2)
print(len(s2))
