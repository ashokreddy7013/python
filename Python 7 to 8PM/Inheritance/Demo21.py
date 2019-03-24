
class Employee:
    def __init__(self,idno=0,name=None,salary=0.0):
        self.idno = idno
        self.name= name
        self.salary = salary
    def display(self):
        print(self.idno)
        print(self.name)
        print(self.salary)

Employee().display()
Employee(101).display()
Employee(101,"Ravi").display()
Employee(101,"Ravi",125000.00).display()
Employee(name="Mohan").display()
Employee(salary=185000.00).display()


