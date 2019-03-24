class A:
    def __init__(self,idno,name):
        self.idno = idno
        self.name = name

class B(A):
    def show(self):
        print(self.idno)
        print(self.name)

b1 = B(101,"Ravi")
b1.show()