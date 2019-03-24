def readPath():
    path = input("Enter Complete Path : ")
    import os.path
    res = os.path.exists(path)
    if res:
        return path
    else:
        return None

def viewAll():
    path = readPath()
    if path == None:
        print("Invalid Path")
    else:
        import os
        list = os.listdir(path)
        for x in list:
            print(x)
def createandWrite():
    path = readPath()
    if path == None:
        print("Invalid Path")
    else:
        fname = input("Enter File Name : ")
        cpath = path+"\\"+fname
        file = open(cpath,"a")
        text = input("Enter Text to File : ")
        file.write(text)
        file.close()
        print("File Created and Data Written")
def openandRead():
    path = readPath()
    if path == None:
        print("Invalid Path")
    else:
        fname = input("Enter File Name : ")
        cpath = path + "\\" + fname
        file = open(cpath)
        print(file.read())
        file.close()
def deleteFile():
    path = readPath()
    if path == None:
        print("Invalid Path")
    else:
        fname = input("Enter File Name : ")
        cpath = path + "\\" + fname
        import os
        os.remove(cpath)
        print("File Deleted")
def main():
    print("File Operations")
    print("1) View All")
    print("2) Create & Write")
    print("3) Open & Read")
    print("4) Delete")
    option = int(input("Select One Option : "))
    if option == 1:
        viewAll()
    elif option == 2:
        createandWrite()
    elif option == 3:
        openandRead()
    elif option == 4:
        deleteFile()
    else:
        print("Invalid Option")

while True:
    main()
    no = int(input("To Continue Press 1 : "))
    if no != 1:
        break
print("Thanks")

