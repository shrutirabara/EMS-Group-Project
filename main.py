import os.path
from employeeFunctions import listEmployee, addEmployee, updateEmployee, removeEmployee, listIds
from departmentFunctions import navigateDepartmentMenu
from jsonConversions import loadJSONEmpObjects, loadJSONDptObjects, appendToEmpJSON, repopulateIdList


def main():
    print("\nWelcome to SOSS")

    # Loading in our JSON Data
    file_name1, file_name2 = "employee_data.json", "departments_data.json"
    employees_list, emp_dictList = [], []
    dpt_list, dpt_dictList = [], []
    loadJSONEmpObjects(employees_list, emp_dictList, file_name1)
    loadJSONDptObjects(dpt_list, dpt_dictList, file_name2)
    idList = []
    repopulateIdList(idList, employees_list)
    print(idList)

    ViewingMenu = True
    while ViewingMenu:
        print("\n1. List All Employees")
        print("2. Add New Employee")
        print("3. Update Employee")
        print("4. Remove Employee")
        print("5. List IDs")
        print("6. View and Update Departments")
        print("7. Exit")

        choice = input("\nSelect # option: ")
        choices = ["1", "2", "3", "4", "5","6","7"]

        if choice not in choices:
            print("\nPlease choose from the following options")
            continue

        match choice:
            case "1":
                listEmployee(employees_list)
            case "2":
                addEmployee(employees_list, dpt_list, idList)
            case "3":
                updateEmployee(employees_list, dpt_list)
            case "4":
                removeEmployee(employees_list)
            case "5":
                listIds(employees_list)
            case "6":
                navigateDepartmentMenu(dpt_list, dpt_dictList)
            case "7":
                ViewingMenu = False

    file_name = "employee_data.json"
    if not os.path.isfile(file_name):
        with open(file_name, "w") as f:
            pass

    for emp in employees_list:
        appendToEmpJSON(file_name1, emp, emp_dictList)


if __name__ == "__main__":
    main()
