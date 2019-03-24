no1 = int(input("1st No :"))
no2 = int(input("2nd No :"))
print("Sum = ",no1+no2)
print("Sub = ",no1-no2)
print("Mul = ",no1*no2)

try:
    print("Div = ",no1/no2)
except ZeroDivisionError as zde:
    print("Don't Enter zero-----",zde)

print("Thanks")
