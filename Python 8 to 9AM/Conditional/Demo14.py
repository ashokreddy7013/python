no = int(input("Enter a No : "))
sum = 0
sum = no%10
no = no//10
while no != 0 :
    r = no%10
    no = no//10
print("SUM = ",(sum+r))
