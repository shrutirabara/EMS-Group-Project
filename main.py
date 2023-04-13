import json
from Employee import Employee
import os.path


# Error Handling Methods

class InvalidStringException(Exception): pass
def enterValidString(message):
    """
    a function that asks an user for a valid string that is alphabetic only,
    will handle errors and keep prompting until valid

    Parameters
    ----------
    message : str
        a message to prompt the user for anything 
    """
    
    StringisInvalid = True
    res = ""
    while StringisInvalid:
        try:
            res = input(message)
            
            if all(x.isalpha() or x.isspace() for x in res):
                StringisInvalid = False
            else:
                print("Bad entry detected!")
                raise InvalidStringException
            
        except InvalidStringException:
            print("Please enter letters only")
    return res

def enterValidNumber(message):
    """
    a function that asks an user for a valid string that is numeric only,
    will handle errors and keep prompting until valid
    ...

    Parameters
    ----------
    message : str
        a message to prompt the user for anything 
    """
    
    StringisInvalid = True
    res = ""
    while StringisInvalid:
        try:
            res = input(message)
            
            if res.isnumeric():
                StringisInvalid = False
            else:
                print("Bad entry detected!")
                raise InvalidStringException
            
        except InvalidStringException:
            print("Please enter numbers only")
    return res

# JSON Custom Serialization and Deserialization Methods

def appendToJSON(fileName, employee, dictList):
    emp_dict = {
        "first name": employee.getFirstName(),
        "last name": employee.getLastName(),
        "id": employee.getEmployeeId(),
        "doe": employee.getDateOfEmployment(),
        "salary": employee.getSalary(),
        "department": employee.getDepartment()
         }
    
    dictList.append(emp_dict)

    json_obj = json.dumps(dictList)

    with open(fileName, "w") as f:
        f.write(json_obj)

def loadJSONObjects(empl_list, emp_dictList, file_name):
    """
    a function that opens a JSON file and loads it into a list, populating a list with dictionaries
    each dictionary is a representation of a Employee Class Object
    we repopulate employees_list by recreating class objects in memory and appending to the list
    ...

    Parameters
    ----------
    emp_list : str
        an empty list of Employee objects, which we will repopulate
    emp_dictList : str
        a list of dictionaries, which we will load our JSON file array into
    file_name : str
        a JSON file name 
    """
    with open(file_name, "r") as f:
        emp_dictList = json.load(f)

    for emp in emp_dictList:
        recreateClassObj = Employee(
            emp["first name"],
            emp["last name"],
            emp["id"], emp["doe"],
            emp["salary"],
            emp["department"]
            )
        # append employee object to empl_list
        empl_list.append(recreateClassObj)


# Menu Functionality Methods

def listEmployee(employees_list):
    for employee in employees_list:
        print("Name:", employee.getFirstName(), employee.getLastName(), "| ID", employee.getEmployeeId(), "| Date of Employment:", employee.getDateOfEmployment(), "| Salary:", employee.getSalary(), "| Department:", employee.getDepartment())

def addEmployee(employees_list):
    # Asking for new Employee data
    name = enterValidString("Enter employee name (first and last): ")
    firstName = name.split()[0].capitalize()
    lastName = name.split()[1].capitalize()
    employeeId = enterValidNumber("Enter the employee ID: ")
    dateOfEmployment = enterValidString("Enter the date of employement: ")
    salary = enterValidNumber("Enter employee salary: ")
    department = enterValidString("Enter department: ")

    # Creating the Employee Object
    emp = Employee(firstName, lastName, employeeId, dateOfEmployment, salary, department)

    # Appending the Object to our Employees List
    employees_list.append(emp)

def updateEmployee(employees_list):
    id = enterValidNumber("\nEnter an ID to update: ")

    employeeFound = False
    for emp in employees_list:
        if emp.getEmployeeId() == id:
            print(f"\nID Match! Employee Found: {emp.getFirstName()} {emp.getLastName()}\n")
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
        choices = ["1","2","3","4","5","6","7"]

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
                emp.setDateOfEmployment(enterValidString("\nNew Date of Employment: "))
            case "5":
                emp.setSalary(enterValidNumber("\nNew Salary: "))
            case "6":
                emp.setDepartment(enterValidString("\nNew Department: "))
            case "7":
                updatingData = False

                    

def main():
    print("\nWelcome to SOSS")

    employees_list, emp_dictList = [], []
    file_name = "employee_data.json"

    loadJSONObjects(employees_list, emp_dictList, file_name)

    ViewingMenu = True
    while ViewingMenu:
        print("\n1. List All Employees")
        print("2. Add New Employee")
        print("3. Update Employee")
        print("4. Remove Employee")
        print("5. Exit")

        choice = input("\nSelect # option: ")
        choices = ["1","2","3","4","5"]

        if choice not in choices:
            print("\nPlease choose from the following options")
            continue

        match choice:
            case "1":
                listEmployee(employees_list)
            case "2":
                addEmployee(employees_list)
            case "3":
                updateEmployee(employees_list)
            case "4":
                print("Remove Employee")
                 #remove employee function
            case "5":
                ViewingMenu = False


    file_name = "employee_data.json"
    if not os.path.isfile(file_name):
        with open(file_name, "w") as f:
            pass
        
    
    for emp in employees_list:
        appendToJSON(file_name, emp, emp_dictList)
        
if __name__ == "__main__":
    main()