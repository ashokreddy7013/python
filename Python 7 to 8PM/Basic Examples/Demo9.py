
class Employee:
    def __init__(self):
        print("I am Default Const")

    def display(self):
        print("I am display Method")

    def __del__(self):
        print("I am disc")

e1 = Employee()
e1.display()
del e1  # deleting object

