class A:
    def display(self):
        print("display of A")
class B:
    def __init__(self):
        print("Default cosnt of B")
class C(A,B):
    def show(self):
        print("show")

c1 = C()
c1.show()
