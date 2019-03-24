class A:
    def __init__(self):
        print("A class Const")

class B(A):
    def __init__(self):
        super().__init__()
        print("B class Const")

B()