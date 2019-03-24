class A:
    def __init__(self,idno):
        self.idno = idno

class B(A):
    def __init__(self,idno,name,salary):
        super().__init__(idno)
        self.name = name
        self.salary = salary

    def show(self):
        print(self.idno)
        print(self.name)
        print(self.salary)

b1 = B(101,"ravi",185000.00)
b1.show()