from Employee import Employee
from errorHandling import enterValidNumber, enterValidString


def addEmployee(employees_list):
    """
    a function that adds an employee object to appends it to the employees_list

    Parameters
    ----------
    employees_list : list
        a list of employees objects
    """
    # Asking for new Employee data
    name = enterValidString("Enter employee name (first and last): ")
    firstName = name.split()[0].capitalize()
    lastName = name.split()[1].capitalize()
    employeeId = enterValidNumber("Enter the employee ID: ")
    dateOfEmployment = enterValidString("Enter the date of employement: ")
    salary = enterValidNumber("Enter employee salary: ")
    department = enterValidString("Enter department: ")

    # Creating the Employee Object
    emp = Employee(firstName, lastName, employeeId,
                   dateOfEmployment, salary, department)

    # Appending the Object to our Employees List
    employees_list.append(emp)
