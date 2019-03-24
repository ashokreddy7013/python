
def outer_fun():
    print("This is outer")
    a = 1000
    def inner_fun():
        print("This is Inner")
        print(a)

    return  inner_fun

outer = outer_fun()
del outer_fun
outer()