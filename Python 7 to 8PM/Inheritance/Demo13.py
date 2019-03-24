class A:
    def m1(self):
        print("m1 of A")
class B(A):
    def m2(self):
        print("m2 of B")
class C(B):
    def m3(self):
        print("m3 of C")

# Creating Object to C class and calling all super class methods
c1 = C()
c1.m3()
c1.m2()
c1.m1()