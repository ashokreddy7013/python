def mytable(tno,eno):
    sno = 1
    while True:
        if sno<=eno:
            mul = tno*sno
            s1 = str(tno)+" X "+str(sno)+" = "+str(mul)
            sno+=1
        else:
            raise StopIteration("TABLE END")
        yield s1

tno =int(input("Enter Table No : "))
eno =int(input("Enter Table End No : "))
try:
    i = mytable(tno,eno)
    while True:
        print(next(i))
except StopIteration as si:
    print(si)