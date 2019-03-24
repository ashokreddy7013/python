
from firebase import firebase as fb

fire = fb.FirebaseApplication("https://django8to9.firebaseio.com/employee",None)
result = fire.get("employee",None)
print(result)


