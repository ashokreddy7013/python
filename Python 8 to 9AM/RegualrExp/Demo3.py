
import re
s1 = "This is naveen from sathya"
result = re.search("naveen",s1)
print(result)
print(result.group())
print(result.start())
print(result.end())
