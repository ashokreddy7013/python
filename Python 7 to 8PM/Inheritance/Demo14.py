class A:
    def __init__(self):
        print("Default Cosnt of A")
class B(A):
    def m2(self):
        print("m2 of B")
class C(B):
    def m3(self):
        print("m3 of C")

c1 = C()
c1.m3()
c1.m2()