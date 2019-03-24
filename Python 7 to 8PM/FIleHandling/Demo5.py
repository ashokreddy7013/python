
try:
    file = open("sample.txt")

    res1 = file.read()
    print(type(res1))

    res2 = file.readline()
    print(type(res2))

    res3 = file.readlines()
    print(type(res3))

    file.close()
except FileNotFoundError:
    print("File not Found")