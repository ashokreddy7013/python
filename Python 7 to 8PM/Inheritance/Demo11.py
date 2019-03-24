class A:
    def m1(self):
        print("m1 of class A")
class B(A):
    def m1(self):
        print("m1 of Class B")
b1 = B()
b1.m1()
