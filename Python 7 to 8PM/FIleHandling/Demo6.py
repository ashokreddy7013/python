
try:
    file = open("sample.txt")
    res = file.readlines()
    for x in res:
        print(x,end=" ")
    file.close()
except FileNotFoundError:
    print("File not Found")