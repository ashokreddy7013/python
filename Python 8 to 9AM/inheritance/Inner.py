class Outer:
    def display(self):
        print("I am Outer")
    class Inner:
        def show(self):
            print("I am Inner")

# Creating Object to Outer class
o = Outer()
o.display()
# o.show() Error

# Creating Object to inner class
i = Outer.Inner()
i.show()