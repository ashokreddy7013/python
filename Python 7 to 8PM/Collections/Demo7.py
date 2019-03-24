
# Working With List Class Methods
#=================================

l1 = [10,20,30,40,50,60,70,15,90,100]
print(l1)
l1.append(110)
print(l1)
l1.insert(3,15)
print(l1)
l1.remove(15)
print(l1)
ele = l1.pop(3)
print(ele)
print(l1)

index_postion = l1.index(50)
print(index_postion)


l2 = [7,5,9,1,4,6,9,3,4,-6,-50]
l2.sort()
print(l2)
l2.reverse()
print(l2)

l3 = l2.copy()
print(l3)
l3.clear()
print(l3)

l1 = [10,20,30]
l2 = [40,50,60]
l1.extend(l2)
print(l1)
print(l2)
