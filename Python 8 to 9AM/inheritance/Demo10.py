class A:
    def __init__(self,idno):
        self.idno = idno

class B(A):
    def __init__(self):
        print("I am Default Const")

B()