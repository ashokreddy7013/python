
l1 = [1,2,3,4,5]
print(list(map((lambda x:x*2),l1)))

print("-----------------")

l1 = [10,20,30,40,50]
l2 = [11,12,13,14,15]
print(l1+l2)
# l3 = []
# for x in range(5):
#     l3.append(l1[x]+l2[x])
# print(l3)

print(list(map((lambda x,y:x+y),l1,l2)))

print("-------------------")
