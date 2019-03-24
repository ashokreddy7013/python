class A:
    def __init__(self,idno,name):
        print("I am Param Const")
        self.idno = idno
        self.name = name

class B(A):
    def display(self):
        print(self.idno)
        print(self.name)

b1 = B(101,"Ravi")
b1.display()