
class Employee:
    def __init__(self,idno=0,name=None):
        self.idno = idno
        self.name = name

    def display(self):
        print(self.idno)
        print(self.name)

e1 = Employee()
e1.display()

e2 = Employee(101)
e2.display()

e3 = Employee(102,"Ravi")
e3.display()

e4 = Employee(name="Murali")
e4.display()

e5 = Employee(name="Murali",idno=103)
e5.display()
