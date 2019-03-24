
import  re
s1 = "Naveen is here"
result = re.match("Naveen",s1)
print(result)
print(result.group())
print(result.start())
print(result.end())
