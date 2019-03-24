
import ExceptionHandling.validation as va

try:
    age = int(input("Enter Age : "))
    res = va.checkAge(age)
    print(res)
except ValueError as v:
    print(v)

