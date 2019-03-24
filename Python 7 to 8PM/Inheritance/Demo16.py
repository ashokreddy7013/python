class A:
    def m1(self):
        print("m1 of A")
class B:
    def m2(self):
        print("m2 of B")
class C(A,B):
    def m3(self):
        print("m3 of C")
c1 = C()
c1.m3()
c1.m2()
c1.m1()
