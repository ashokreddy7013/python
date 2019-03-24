class A:
    def m1(self):
        print("M1 of A")
class B:
    def m2(self):
        print("M2 of B")
class C(A,B):
    def m3(self):
        print("M3 of C")

c1 = C()
c1.m3()
c1.m2()
c1.m1()