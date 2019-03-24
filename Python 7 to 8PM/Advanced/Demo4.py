class MyTable:
    def __init__(self,tno=0,eno=0):
        self.tno = tno
        self.eno = eno
    def __iter__(self):
        self.sno = 0
        return self
    def __next__(self):
        self.sno += 1
       # if self.sno <= self.eno:
        mul = self.tno * self.sno
        s1 = str(self.tno)+" X "+str(self.sno)+" = "+str(mul)
        return s1
        #else:
            #raise StopIteration("End")



# m1 = MyTable(5,5)
# r = m1.__iter__()
# print(r.__next__())
# print(r.__next__())
# print(r.__next__())
# print(r.__next__())
# print(r.__next__())
# print(r.__next__())


