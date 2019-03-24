try:
    file = open("sample.txt")
    result = file.read()
    print(result)
    file.close()
except FileNotFoundError:
    print("File not Found")