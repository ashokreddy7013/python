class Employee:
    def __init__(self):
        print("This is default const")
    def display(self):
        print("This is display")
    def __del__(self):
        print("This is Disct")

e1 = Employee()
e1.display()
e1.display()
e1.display()
e1.display()
del e1


