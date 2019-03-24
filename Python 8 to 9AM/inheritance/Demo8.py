class A:
    def __init__(self):
        print("I am Default Const of A")

class B(A):
    def __init__(self):
        super().__init__() # Calling A Class Const
        print("I am Default Const of B")

B()

