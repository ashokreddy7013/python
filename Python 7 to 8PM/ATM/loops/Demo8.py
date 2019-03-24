no = int(input("Enter No : "))
sum = no%10
no = no//10
r=0
while(no!=0):
    r = no%10
    no=no//10
print(sum+r)