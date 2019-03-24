class A:
    def __init__(self):
        print("I am Default Const of A")

class B(A):
    def show(self):
        print("I am Show")

b1 = B()
b1.show()