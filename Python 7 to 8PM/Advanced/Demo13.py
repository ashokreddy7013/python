
def outer_function():
    print("Outer Function")
    a = 1000 # Local Variable
    def inner_function():
        print("Inner Function")
        print(a)
    inner_function() # Calling Inner Function

outer_function()
