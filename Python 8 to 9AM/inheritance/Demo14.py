class A:
    def display(self):
        print("I am display of A")

class B:
    def display(self):
        print("I am display of B")

class C(B,A):
    def show(self):
        print("I am show of C")

c1 = C()
c1.show()
c1.display()