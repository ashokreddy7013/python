class Employee:
    comp_name = "sathya"
    comp_cno = 9876543210

    @staticmethod
    def displayCompInfo():
        print(Employee.comp_name)
        print(Employee.comp_cno)

Employee.displayCompInfo()
