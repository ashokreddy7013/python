class A:
    def __init__(self):
        print("Default const of A")

class B(A):
    def show(self):
        print("I am show")

class C(B):
    def display(self):
        print("I am display")

c1 = C()
c1.display()
c1.show()