import os.path
from employeeFunctions import listEmployee, addEmployee, updateEmployee, removeEmployee, listIds
from jsonConversions import loadJSONObjects, appendToJSON

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
        print("5. List IDs")
        print("5. Exit")

        choice = input("\nSelect # option: ")
        choices = ["1", "2", "3", "4", "5","6"]

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
                removeEmployee(employees_list)
            case "5":
                listIds(employees_list)
            case "6":
                ViewingMenu = False



    file_name = "employee_data.json"
    if not os.path.isfile(file_name):
        with open(file_name, "w") as f:
            pass

    for emp in employees_list:
        appendToJSON(file_name, emp, emp_dictList)


if __name__ == "__main__":
    main()
