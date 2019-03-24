
class First:
    def calc(self,no1,no2):
        print(no1+no2)
        print(no1-no2)

class Second(First):
    def calc(self,no1,no2):
        super().calc(no1,no2)
        print(no1*no2)
        print(no1/no2)

class Three(Second):
    def calc(self,no1,no2):
        super().calc(no1,no2)
        print(no1%no2)
        print(no1//no2)

t1 = Three()
t1.calc(10,5)