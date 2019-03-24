
#from ExceptionHandling import validator

#from ExceptionHandling.validator import*
import validator as v

try:
    a = int(input("Enter Age : "))
    res = v.checkAge(a)
    print(res)
    cno = input("Enter Contact No : ")
    res1 = v.checkContactNo(cno)
    print(res1)
except ValueError as ve:
    print(ve)
print("Thanks")
