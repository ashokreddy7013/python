class A:
    def show(self):
        print("I am show of A")

class B(A):
    def show(self):
        print(" B Class Show")

b1 = B()
b1.show()