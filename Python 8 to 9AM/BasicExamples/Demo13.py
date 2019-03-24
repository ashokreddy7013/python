class Employee:
    def __init__(self,idno,name):
        print("Object Created")
        self.idno = idno
        self.name = name

    def display(self):
        print(self.idno)
        print(self.name)

    def __del__(self):
        print("Object Deleted")

e1 = Employee(101,"Ravi")
e1.display()
del e1 # deleting Object
# e1.display() Error
