class A:
    def __init__(self,no1,no2):
        self.a = no1
        self.b = no2
class B(A):
    def __init__(self):
        super().__init__(100,500)
        print("I am Default")
    def show(self):
        print(self.a)
        print(self.b)
b1 = B()
b1.show()