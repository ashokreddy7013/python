

import re
s1 = "Hello this is sathya Contact us on 100"
result = re.findall(r"\w",s1)
print(result)

print("-------------")

s1 = "Hello@ this is N@v$$n"
result = re.findall(r"\W",s1)
print(result)

print("------------------")

s1 = "Hello this is sathya Contact us on 100"
result = re.findall(r"\w*",s1)
print(result)

print("------------------")

s1 = "Hello this is sathya Contact us on 100"
result = re.findall(r"\w+",s1)
print(result)