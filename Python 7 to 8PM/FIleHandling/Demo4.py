try:
    file = open("sample.txt")
    text = file.readline()
    for x in text:
        print(x,end=" ")
    file.close()
except FileNotFoundError:
    print("File not Found")
