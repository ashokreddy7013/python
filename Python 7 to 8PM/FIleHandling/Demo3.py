
try:
    file = open("sample.txt")
    result = file.readline()
    print(result)
    result = file.readline()
    print(result)
    file.close()
except FileNotFoundError:
    print("File not Found")