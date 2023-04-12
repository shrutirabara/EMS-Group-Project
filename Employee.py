class Employee:
    # Instance Data Members
    def __init__(self, firstName, lastName, employeeId, dateOfEmployment, salary, department):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__employeeId = employeeId
        self.__dateOfEmployment = dateOfEmployment
        self.__salary = salary
        self.__department = department

    # Getter Methods

    def getFirstName(self):
        return self.__firstName
    def getLastName(self):
        return self.__lastName
    def getEmployeeId(self):
        return self.__employeeId
    def getDateOfEmployment(self):
        return self.__dateOfEmployment
    def getSalary(self):
        return self.__salary
    def getDepartment(self):
        return self.__department

    # Setter Methods

    def setFirstName(self, fnInput):
        self.__firstName = fnInput
        print(f"First Name set to '{fnInput}'")
    def setLastName(self, lnInput):
        self.__lastName = lnInput
    def setEmployeeId(self, idInput):
        self.__employeeId = idInput
    def setDateOfEmployment(self, doeInput):
        self.__dateOfEmployment = doeInput
    def setSalary(self, salaryInput):
        self.__salary = salaryInput
    def setDepartment(self, dInput):
        self.__department = dInput


# Steven = Employee("steven", "chan", "23", "April 13th, 2023", "75000", "Web Development")

# print(Steven.getFirstName(), Steven.getLastName(), Steven.getEmployeeId(), Steven.getDateOfEmployment(), Steven.getSalary(), Steven.getDepartment())

# Steven.setDateOfEmployment("April 14th, 2023")

# Sadie = Employee("sadie", "kc", "12" "June 5th, 2022", "65000", "Data Administrator")
# print(Sadie.getFirstName, Steven.getLastName(), Sadie.getEmployeeId, Sadie.getDateOfEmployment, Sadie.getSalary, Sadie.getDepartment)

    
