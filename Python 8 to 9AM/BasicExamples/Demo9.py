
class Employee:
    comp_name = "sathya" # static variable
    @classmethod
    def show(cls):
        print(cls)
        print("I am Class Method")
        # calling static variables
        print(Employee.comp_name)
        print(cls.comp_name)


# calling class Method
Employee.show()