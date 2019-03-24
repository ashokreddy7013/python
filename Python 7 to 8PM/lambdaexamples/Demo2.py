
# Using if else in lambda

a = int(input("1st No : "))
b = int(input("2nd No : "))

check = lambda no1,no2:no1 if no1>no2 else no2
print(check(a,b))