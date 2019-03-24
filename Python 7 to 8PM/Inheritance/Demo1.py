class A:
    def display(self):
        print("This is display of class A")

class B(A):
    def show(self):
        print("I am Show")

b1 = B()
b1.show()
b1.display()


