# Using if else in lambda

a = int(input("1st No : "))
b = int(input("2nd No : "))
c = int(input("3nd No : "))

check = lambda no1,no2,no3:no1 if no1>no2 and no1>no3 else no2 if no2>no1 and no2>no3 else no3

print(check(a,b,c))
