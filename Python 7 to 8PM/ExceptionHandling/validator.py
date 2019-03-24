
def checkAge(age):
    if age>=18 and age<=60:
        return "Valid Age"
    else:
        raise ValueError("Invalid Age")

def checkContactNo(cno):
    if len(cno) == 10:
        if cno[0]=="9" or cno[0]=="8" or cno[0]=="7":
            return "Valid Contact"
        else:
            raise ValueError("Invalid Contact No")
    else:
        raise ValueError("Contact No Must be 10 Digit Only")