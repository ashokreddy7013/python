
try:
    file = open("sample.txt")
    print(file)
    file.close()
except FileNotFoundError as fne:
    #print(fne)
    print("No File Found")
