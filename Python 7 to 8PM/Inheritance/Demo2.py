class A:
    def display(self):
        self.val1 = 1000

class B(A):
    def show(self):
        print(self.val1)

b1 = B()
b1.display()
b1.show()