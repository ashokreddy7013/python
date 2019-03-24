class A:
    @staticmethod
    def mA():
        print("I am static of A")

class B(A):
    @staticmethod
    def mB():
        print("I am static of B")

B.mB() # Calling B Class method
B.mA() # Calling A Class method