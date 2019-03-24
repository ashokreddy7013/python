name = input("Enter Name : ")
res = iter(name)
while True:
    try:
        print(next(res),end=" ")
    except StopIteration:
        break