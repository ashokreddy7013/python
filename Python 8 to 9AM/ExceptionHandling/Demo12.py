
import ExceptionHandling.validation as va

try:
    cno = input("Enter Contact No : ")
    res = va.checkContactNo(cno)
    print(res)
except ValueError as v:
    print(v)
