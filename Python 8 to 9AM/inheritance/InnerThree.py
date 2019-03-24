class OuterA:
    def m1(self):
        print("m1 of OuterA")
    class InnerA:
        def m2(self):
            print("m2 of InnerA")


class OuterB(OuterA.InnerA):
    def show(self):
        print("This is show of OuterB")

    def m2(self):
        print("I am from OuterB")

o1 = OuterB()
o1.show()
o1.m2()