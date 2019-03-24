try:
    file = open("sample.txt")
    for x in file:
        #print(x)
        print(x,end=" ")
    file.close()
except FileNotFoundError:
    print("File not Found")

