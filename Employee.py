class Employee:
    """
    A class used to represent an Employee
    ...

    Private Attributes
    ----------
    __firstName : str
        a string representing the first name of an Employee
    __lastName : str
        a string reprsenting the last name of an Employee
    __employeeId : int
        a employee id that is unique and represents an Employee
    __dateOfEmployment : str
        a string that represents the date of employment
    __salary : int
        a int number representing Employee salary
    __deparment : str
        a string that represents the deparment
    """
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


    
