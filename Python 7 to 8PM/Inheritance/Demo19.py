
class A:
    def m1(self):
        print("m1 of A")

class B(A):
    def m2(self):
        print("m2 of B")

class C(A):
    def m3(self):
        print("m3 of C")

b1 = B()
b1.m1()
b1.m2()

c1 = C()
c1.m1()
c1.m3()
