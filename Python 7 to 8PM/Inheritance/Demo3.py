# Example on instance methods
class A:
    def display(self):
        print("display of A Class")
class B(A):
    def show(self):
        print("show of B Class")

b1 = B()
b1.show()
b1.display()
