class Employee:
    comp_name = "sathya"
    __comp_cno = 9052492329 #Private
    def show(self):
        print(Employee.comp_name)
        print(Employee.__comp_cno)

e1 = Employee()
e1.show()

print(Employee.comp_name)
print(Employee.__comp_cno)