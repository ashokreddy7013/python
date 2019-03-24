class A:
    def m1(self):
        print("m1 of A")

class B:
    def m2(self):
        print("m2 of B")

class Outer(A):
    def display(self):
        print("display of Outer")

    class Inner(B):
        def show(self):
            print("show of Inner")

        def m2(self):
            print("I am Inner m2")

o1 = Outer()
o1.display()
o1.m1()

i1 = Outer.Inner()
i1.show()
i1.m2()