class Employee:
    def display(self,idno=0,name=None,salary=0.0):
        print(idno)
        print(name)
        print(salary)

e1 = Employee()
e1.display()
e1.display(101)
e1.display(101,"Ravi")
e1.display(101,"Ravi",125000.00)
e1.display(name="Krishna")
e1.display(salary=185000.00)

