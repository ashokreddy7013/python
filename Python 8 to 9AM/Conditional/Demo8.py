
for x in range(2,21,2):
    print(x,end=" ")
else:
    print("Even No's")
print("Thanks")


for x in range(2,21,2):
    if x == 10:
        break
    print(x)
else:
    print("Even No's")
print("Thanks")

l1=[10,20,30,40,50]

for x in l1:
    print(x)

for x in l1[0:3]:
    print(x)

for x in l1[::-1]:
    print(x)