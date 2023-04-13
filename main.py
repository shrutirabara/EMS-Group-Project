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
        print(employee.getFirstName(), employee.getLastName(), employee.getEmployeeId(), employee.getDateOfEmployment(), employee.getSalary(), employee.getDepartment())

def addEmployee(employees_list):
    # name = input("Enter employee name (first and last): ")
    name = enterValidString("Enter employee name (first and last): ")
    firstName, lastName = name.split()[0], name.split()[1]
    firstName = firstName.capitalize()
    lastName = lastName.capitalize()

    employeeId = input("Enter the employee ID: ")
    dateOfEmployment = input("Enter the date of employement: ")
    salary = input("Enter employee salary: ")
    
    department = enterValidString("Enter department: ")

    emp = Employee(firstName, lastName, employeeId, dateOfEmployment, salary, department)

    print(emp.getFirstName(), emp.getLastName(), emp.getEmployeeId(), emp.getDateOfEmployment(), emp.getSalary(), emp.getDepartment())

    employees_list.append(emp)

def updateEmployee(id):
    pass




def main():
    print("Welcome to SOSS\n")

    employees_list, emp_dictList = [], []
    file_name = "employee_data.json"

    loadJSONObjects(employees_list, emp_dictList, file_name)

    ViewingMenu = True
    while ViewingMenu:
        print("1. List All Employees")
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
                print("Update Employee")
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