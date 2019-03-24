import copy as cp
l1 = [[10,20,30],[40,50,60],[70,80,90]]
l2 = cp.copy(l1)
print("L1 :",l1)
print("L2 :",l2)
l2[0]=['a','b']
print('l2:',l2)
print('L1:',l1)
l2[1][0]='D'
print("deep copy L2:",l2)
print('deep copy L1:',l1)




