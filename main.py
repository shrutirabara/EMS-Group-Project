import json
import Employee

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


def main():
    
    with open("employees_data.json", 'r') as f:
        jsonData = json.load(f)
    employees_list = list(jsonData.values())
    
    while True:
        print("1. Add New Employee")
        print("2. Update Employee")
        print("3. Remove Employee")
        print("4. List All Employees")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter employee name (first and last): ")
            firstName, lastName = name.split()
            firstName = firstName.capitalize()
            lastName = lastName.capitalize()

            employeeId = input("Enter the employee ID: ")
            dateOfEmployment = input("Enter the date of employement: ")
            salary = input("Enter employee salary: ")
            
            employee = {
                "firstName": firstName,
                "lastName": lastName,
                "employeeId": employeeId,
                "dateOfEmployment": dateOfEmployment,
                "salary": salary
            }
            employees_list.append(employee)
            
        elif choice == "2":
            print("2. Update Employee")
        elif choice == "3":
            print("3. Remove Employee")
        elif choice == "4":
            print("4. List All Employees")
        elif choice == "5":
            print("Exiting menu")
            break

        else:
            print("Invalid choice")

   

        

