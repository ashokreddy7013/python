
class A:            #(using instance methods)
    def display(self):
        print("I am A Class Method")

class B(A):
    def show(self):
        print("I am B Class Method")

b1 = B() # Object is Created to B Class
b1.display() # A Class Method
b1.show() # B Class Method

