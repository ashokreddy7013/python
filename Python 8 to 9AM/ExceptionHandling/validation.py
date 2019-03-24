
def checkAge(age):
    if age>=23 and age<=60:
        return "Valid Age"
    else:
        raise ValueError("Invalid Age")

def checkContactNo(cno):
    contact = str(cno)
    if len(contact) != 10:
        raise ValueError("Must be 10 digit")
    else:
        if contact[0] in "9876":
            return "Valid Contact"
        else:
            raise ValueError("Invalid Contact")







