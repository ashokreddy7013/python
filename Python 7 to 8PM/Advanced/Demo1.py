#
# for x in [10,20,30,40,50]:
#     print(x)
# print("--------------------")

l1 = [10,20,30,40,50]
res = iter(l1)
print(res.__next__())
print(res.__next__())
print(next(res))
print(next(res))
print(next(res))

