class A:
    def __init__(self):
        print("Default Cosnt of A")
class B(A):
    def __init__(self):
        super().__init__()
        print("Default Cosnt of B")
class C(B):
    def __init__(self):
        print("Default Cosnt of C")
        super().__init__()

C()