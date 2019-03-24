
tno =int(input("Enter Table No : "))
eno =int(input("Enter Table End No : "))

gen = (tno*x for x in range(1,eno+1))
for x in range(1,eno+1):

    print(tno," X ",x," = ",next(gen))


