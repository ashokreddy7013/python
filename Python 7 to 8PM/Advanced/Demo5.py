tno = int(input("Table No : "))
eno = int(input("End No : "))
from Advanced.Demo4 import MyTable
m1 = MyTable(tno,eno).__iter__()
while True:
    try:
        print(next(m1))
    except StopIteration as se:
        print(se)
        break