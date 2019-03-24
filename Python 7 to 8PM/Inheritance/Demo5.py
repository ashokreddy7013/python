class A:
    def __init__(self):
        print("Default Constructor of A")

class B(A):
    def show(self):
        print("show of B")

b1 = B()
b1.show()