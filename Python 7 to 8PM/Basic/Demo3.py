
# WAP to validate username and password

uname = input("Username : ")
upass = input("Password : ")
if uname == "sathya":
    if upass == "tech":
        print("Valid User")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")
print("Thanks")
