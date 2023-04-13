from Employee import Employee
from errorHandling import enterValidNumber, enterValidString

def listEmployee(employees_list):
    """
    a function that lists all attributes from each employee object from the employees_list

    Parameters
    ----------
    employees_list : list
        a list of employees objects
    """
    for employee in employees_list:
        print("")
        print(employee.getFirstName(), employee.getLastName(), employee.getEmployeeId(
        ), employee.getDateOfEmployment(), employee.getSalary(), employee.getDepartment())


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
    dateOfEmployment = input("Enter the date of employement: ")
    salary = enterValidNumber("Enter employee salary: ")
    department = enterValidString("Enter department: ")

    # Creating the Employee Object
    emp = Employee(firstName, lastName, employeeId,
                   dateOfEmployment, salary, department)

    # Appending the Object to our Employees List
    employees_list.append(emp)


def updateEmployee(employees_list):
    """
    a function that updates an employee object from the employees_list based on an attribute

    Parameters
    ----------
    employees_list : list
        a list of employees objects
    """
    id = enterValidNumber("\nEnter an ID to update: ")

    employeeFound = False
    for emp in employees_list:
        if emp.getEmployeeId() == id:
            print(
                f"\nID Match! Employee Found: {emp.getFirstName()} {emp.getLastName()}\n")
            employeeFound = True
        else:
            pass

    updatingData = True
    while employeeFound and updatingData:
        print("Which information would you like to change?\n")
        print("1. First Name")
        print("2. Last Name")
        print("3. ID")
        print("4. Date of Employment")
        print("5. Salary")
        print("6. Department")
        print("7. Done")

        choice = input("\nSelect # option: ")
        choices = ["1", "2", "3", "4", "5", "6", "7"]

        if choice not in choices:
            print("\nPlease choose from the following options")
            continue

        match choice:
            case "1":
                emp.setFirstName(enterValidString("\nNew first name: "))
            case "2":
                emp.setLastName(enterValidString("\nNew last name: "))
            case "3":
                emp.setEmployeeId(enterValidNumber("\nNew ID: "))
            case "4":
                emp.setDateOfEmployment(input("\nNew Date of Employment: "))
            case "5":
                emp.setSalary(enterValidNumber("\nNew Salary: "))
            case "6":
                emp.setDepartment(enterValidString("\nNew Department: "))
            case "7":
                updatingData = False

def removeEmployee(employees_list):
    
    while True:
        try:
            RemoveID = enterValidNumber("Please enter the Employee ID you would like to remove: ")
            check = input("Are you sure you want to remove employee? Y or N: ").lower()
            if check == "y":
                for employee in employees_list:
                    if RemoveID == employee.getEmployeeId():
                        employees_list.remove(employee)
                        
                        print("Successfully deleted")
                        listEmployee(employees_list)
                  
            elif check == "n":
                again = input("Would you like to continue? Y or N: ").lower()
                if again == "y":
                    continue
                elif again == "n":
                    break
                else:
                    print("That is not a valid answer")
                    continue
            else:
                print("That is not a valid answer")
                continue
        except ValueError:
            print("that is not a valid ID")
            continue