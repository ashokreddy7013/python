class A:
    def show(self):
        print("show of A")

class B:
    def show(self):
        print("show of B")

class C(A,B):
    def display(self):
        print("display of C")

c1 = C()
c1.display()
c1.show()