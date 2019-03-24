l1 = [1,2,3,4,5,6,7,8,9,10]
print(list(filter((lambda x:x%2 == 0),l1)))
print("-----------------")

st = input("Enter String : ")
print(len(list(filter((lambda x:x=='a'),st))))
