class A:
    def show(self):
        print("show of A class")
class B:
    def smaple(self):
        print("smaple of B Class")
class C:
    def __init__(self):
        print("C Class")
class D(B,C,A):
    def display(self):
        print("display of D")

D()
