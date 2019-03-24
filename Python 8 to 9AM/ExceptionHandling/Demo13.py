

import ExceptionHandling.UserderfinedException as ue

def checkAge(age):
    if age>=23 and age<=60:
        return "Valid Age"
    else:
        raise ue.MyException("Invalid Age")


try:
    age = int(input("Enter Age : "))
    res = checkAge(age)
    print(res)
except ue.MyException as my:
    print(my)
