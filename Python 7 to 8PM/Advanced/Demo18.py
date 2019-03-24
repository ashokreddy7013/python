class Employee():
    def __init__(self,idno,name):
        self.idno = idno
        self.name = name
    def display(self):
        print(self.idno)
        print(self.name)
        
emp = Employee(101,"Ravi")
emp.display()