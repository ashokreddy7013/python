class Employee:
    def __init__(self):
        print("This is default const")
    def display(self):
        print("This is display")
    def __del__(self):
        print("This is Disct")

Employee().display()
