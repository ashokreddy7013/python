
from ExceptionHandling import validation as va

u_age = int(input("Enter Age"))
u_cno = input("Enter Contact ")
try:
    age = va.checkAge(u_age)
    print(age," Is Valid")
    cno = va.checkContact(u_cno)
    print(cno," Is Valid")
except ValueError as ve:
    print(ve)