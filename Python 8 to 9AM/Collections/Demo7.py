
my_friends = ["Ravi","Kumar","Prasad","Rama","Krish","mohan"]
ur_frineds = ["Rani","Kumar","venkat","Rama","krish","Prasad","Kanna","Banna"]

for x in my_friends:
    if x in ur_frineds:
        print(x)
print("------------------")
for x in my_friends:
    if x not in ur_frineds:
        print(x)