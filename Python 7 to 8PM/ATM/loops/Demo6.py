
a = 1
while(a<=10):
    print(a)
    a+=1
print("Thanks")
print("-----------------")
ans = 0
no = int(input("Enter No :"))
while(no!=0):
    r = no%10
    no = no//10
    ans = ans*10+r
print(ans)


