def Outer_fun():
    print("Outer Function")
    def Inner_fun():
        print("Inner Function")
        def Inner_Inner_fun():
            print("Inner inner Function")
        Inner_Inner_fun()
    Inner_fun()

Outer_fun()
