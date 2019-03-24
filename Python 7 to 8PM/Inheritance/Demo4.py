# Example on static methods
class A:
    @staticmethod
    def m1():
        print("static of m1 from A")
class B(A):
    @staticmethod
    def m2():
        print("static of m2 from B")
B.m2()
B.m1()