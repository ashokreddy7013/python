try:
    no1 = int(input("1st No :"))
    no2 = int(input("2nd No :"))
    print("sum = ",no1+no2)
    print("div = ",no1/no2)
except ZeroDivisionError as zde:
    print(zde)
except ValueError as ve:
    print("Invalid Input")
