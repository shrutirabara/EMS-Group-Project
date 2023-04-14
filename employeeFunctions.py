import time
from Employee import Employee
from errorHandling import enterValidNumber, enterValidString
from departmentFunctions import selectDepartment


def listEmployee(employees_list):
    """
    a function that lists all attributes from each employee object from the employees_list

    Parameters
    ----------
    employees_list : list
        a list of employees objects
    """
    for employee in employees_list:
        print("Name:", employee.getFirstName(), employee.getLastName(), "| ID:", employee.getEmployeeId(), "| Date of Employment:",
              employee.getDateOfEmployment(), "| Salary:", employee.getSalary(), "| Department:", employee.getDepartment())


def addEmployee(employees_list, departments):
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

    dpt_obj = selectDepartment(departments)

    # Creating the Employee Object
    emp = Employee(firstName, lastName, employeeId,
                   dateOfEmployment, salary, dpt_obj.getDptName())

    # Appending the Object to our Employees List
    employees_list.append(emp)


def updateEmployee(employees_list, departments):
    """
    a function that updates an employee object from the employees_list based on an attribute

    Parameters
    ----------
    employees_list : list
        a list of employees objects
    """
    id = enterValidNumber("\nEnter an ID to update: ")

    idFound = False
    for emp_obj in employees_list:
        if emp_obj.getEmployeeId() == id:
            print(
                f"\nID Match! Employee Found: {emp_obj.getFirstName()} {emp_obj.getLastName()}\n")
            emp = emp_obj
            idFound = True
        else:
            pass

    if not idFound:
        print("\nNo Match! Returning to previous menu\n")
        time.sleep(1)
        return

    updatingData = True
    while updatingData:
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
            print("\nPlease choose from the following options\n")
            continue

        match choice:
            case "1":
                print(emp.getFirstName())
                emp.setFirstName(enterValidString("\nNew first name: "))
            case "2":
                print(emp.getLastName())
                emp.setLastName(enterValidString("\nNew last name: "))
            case "3":
                print(emp.getEmployeeId())
                emp.setEmployeeId(enterValidNumber("\nNew ID: "))
            case "4":
                print(emp.getDateOfEmployment())
                emp.setDateOfEmployment(input("\nNew Date of Employment: "))
            case "5":
                print(emp.getSalary())
                emp.setSalary(enterValidNumber("\nNew Salary: "))
            case "6":
                print(emp.getDepartment())
                dpt_obj = selectDepartment(departments)
                emp.setDepartment(dpt_obj.getDptName())
            case "7":
                updatingData = False


def removeEmployee(employees_list):

    while True:
        try:
            RemoveID = enterValidNumber(
                "Please enter the Employee ID you would like to remove: ")
            check = input(
                "Are you sure you want to remove employee? Y or N: ").lower()
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


def listIds(employees_list):
    ids = [(emp.getFirstName(), emp.getEmployeeId()) for emp in employees_list]
    print(f"\nHere is a list of all our employee IDs: \n{ids}")
