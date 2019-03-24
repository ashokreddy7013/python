
no = int(input("Enter No : "))
sum=0
while no!=0:
    r=no%10
    sum=sum+r
    no=no//10

print(sum)