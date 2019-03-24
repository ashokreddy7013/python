class Employee:
    comp_name = "sathya"
    def __init__(self,idno,na):
        self.idno = idno
        self.name = na
    def display(self):
        print(self.comp_name)
        print(self.idno)
        print(self.name)

e1 = Employee(101,"Ravi")
e1.display()

e2 = Employee(102,"Krishna")
e2.display()