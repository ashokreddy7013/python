class A:
    def sample(self):
        print("I am Sample")

class B(A):
    def m1(self):
        print("m1 of B")

class C(A):
    def m2(self):
        print("m2 of C")


b1 = B()
b1.m1()
b1.sample()


c1 = C()
c1.m2()
c1.sample()