class Employee:
    def assign(self,idno,name):
        self.idno = idno
        self.name = name
    def display(self):
        print("IDNO = ",self.idno)
        print("NAME = ",self.name)

# Creating Object to Employee class
emp = Employee()
emp.assign(101,"Ravi")
emp.display()

