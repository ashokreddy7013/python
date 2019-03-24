
no = int(input("Enter a No : "))
rev = 0
while no != 0:
    r = no%10
    no = no//10
    rev = rev*10+r
print("Given No in Rev = ",rev)