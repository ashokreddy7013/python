
class Employee:
    def __init__(self,idno,name):
        self.idno = idno
        self.name = name

    def display(self):
        print(self.idno)
        print(self.name)

e1 = Employee(101,"Ravi")
e1.display()

e2 = Employee(102,"Kumar")
e2.display()