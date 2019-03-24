
import re
s1 = "98765@43210"
res = re.match(r"\d{10}",s1)
if res:
    print("Valid")
else:
    print("Invalid")