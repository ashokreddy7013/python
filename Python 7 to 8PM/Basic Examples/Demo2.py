class Employee:
    comp_name = "sathya"
    comp_cno = 9052492329
    def display(self):
        print(Employee.comp_name)
        print(Employee.comp_cno)

# Creating Object to Employee Class
emp1 = Employee()
# Calling Employee Class Method
emp1.display()
# Calling Static variables using object variable
print(emp1.comp_name)
print(emp1.comp_cno)
# Calling Static Variables using Class Name
print(Employee.comp_name)
print(Employee.comp_cno)