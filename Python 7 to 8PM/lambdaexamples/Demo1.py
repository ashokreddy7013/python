# Example with 0 argument
lam = lambda :print("This is lamda")
lam()

# Example with 1 argument
lam = lambda no1:print(" value = ",no1)
lam(10)

# Example with multi Arguments
sum = lambda no1,no2:no1+no2
print(sum(10,20))

# Example with default Arguments

sum = lambda no1=10,no2=20 : no1+no2
print(sum())#30
print(sum(59))#79
print(sum(5,1))#6
print(sum(no2=99))#109

# Using if else in lambda

