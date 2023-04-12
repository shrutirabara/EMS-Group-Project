import json
from Employee import Employee
import os.path

# Class Employee
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

def addEmployee(employees_list):
    name = input("Enter employee name (first and last): ")
    firstName, lastName = name.split()[0], name.split()[1]
    firstName = firstName.capitalize()
    lastName = lastName.capitalize()

    employeeId = input("Enter the employee ID: ")
    dateOfEmployment = input("Enter the date of employement: ")
    salary = input("Enter employee salary: ")
    
    department = input("Enter department: ")

    emp = Employee(firstName, lastName, employeeId, dateOfEmployment, salary, department)

    print(emp.getFirstName(), emp.getLastName(), emp.getEmployeeId(), emp.getDateOfEmployment(), emp.getSalary(), emp.getDepartment())

    employees_list.append(emp)

def listEmployee(employees_list):
    for employee in employees_list:
        print(employee.getFirstName(), employee.getLastName(), employee.getEmployeeId(), employee.getDateOfEmployment(), employee.getSalary(), employee.getDepartment())


def append_to_file(fileName, employee, dictList):
    emp_dict = {
        "first name": employee.getFirstName(),
        "last name": employee.getLastName(),
        "id": employee.getEmployeeId(),
        "doe": employee.getDateOfEmployment(),
        "salary": employee.getSalary(),
        "deparment": employee.getDepartment()
         }
    
    dictList.append(emp_dict)

    json_obj = json.dumps(dictList)

    with open(fileName, "w") as f:
        f.write(json_obj)


def main():
    
    employees_list = []
    emp_dictList = []
    
    file_name = "employee_data.json"
    with open(file_name, "r") as f:
        emp_dictList = json.load(f)

    
    while True:
        print("1. Add New Employee")
        print("2. Update Employee")
        print("3. Remove Employee")
        print("4. List All Employees")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            addEmployee(employees_list)
            
        elif choice == "2":
            print("2. Update Employee")

        elif choice == "3":
            print("3. Remove Employee")
        elif choice == "4":
            listEmployee(employees_list)
        elif choice == "5":
            print("Exiting menu")
            break

        else:
            print("Invalid choice")

    file_name = "employee_data.json"
    if not os.path.isfile(file_name):
        with open(file_name, "w") as f:
            pass
        
    
    for emp in employees_list:
        append_to_file(file_name, emp, emp_dictList)
        
    
if __name__ == "__main__":
    main()