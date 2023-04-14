import os.path, time
from Department import Department
from errorHandling import enterValidNumber, enterValidString
from jsonConversions import appendToDptJSON

def listDepartments(departments):
    count = 1
    print("")
    for dpt in departments:
        print(f"{count}. Name: {dpt.getDptName()} | Budget: {dpt.getDptBudget()} | Phone: {dpt.getDptNumber()}")
        count += 1
    print("")
    


def addDepartments(departments):
    name = enterValidString("Enter Department Name: ")
    budget = enterValidNumber(f"Enter {name} Budget: ")
    phone = enterValidNumber(f"Enter {name} Phone #: ")

    # Creating the Department Object
    dpt_obj = Department(name, budget, phone)

    # Appending the Object to our Employees List
    departments.append(dpt_obj)


def selectDepartment(departments):
    """
    a function that lists all Department object from the departments list based on the name,
    prompts a user to select a department
    
    Parameters
    ----------
    departments : list
        a list of Department objects
    
    Returns
    ----------
    department : object
        a Department object    
    """
    listDepartments(departments)
    while True:
        dpt_num = int(enterValidNumber("Select Department #: ")) - 1
        if 0 <= dpt_num < len(departments):
            return departments[dpt_num]


def updateDepartments(departments):
    """
    a function that updates a department object from the departments list based on the name

    Parameters
    ----------
    departments : list
        a list of Department objects
    """
    name = enterValidString("\nEnter a Deparment Name to update: ")

    nameFound = False
    for dpt_obj in departments:
        if dpt_obj.getDptName() == name:
            print(
                f"\nName Match! Department Found: {dpt_obj.getDptName()}\n")
            dpt = dpt_obj
            nameFound = True
        else:
            pass

    if not nameFound:
        print("\nNo Match! Returning to previous menu\n")
        time.sleep(1)
        return

    updatingData = True
    while updatingData:
        print("Which information would you like to change?\n")
        print("1. Name")
        print("2. Budget")
        print("3. Phone #")
        print("4. Done")

        choice = input("\nSelect # option: ")
        choices = ["1", "2", "3", "4"]

        if choice not in choices:
            print("\nPlease choose from the following options\n")
            continue

        match choice:
            case "1":
                print(dpt.getDptName())
                dpt.setDptName(enterValidString("\nNew Department name: "))
            case "2":
                print(dpt.getDptBudget())
                dpt.setDptBudget(enterValidNumber("\nNew Department budget: "))
            case "3":
                print(dpt.getDptNumber())
                dpt.setDptNumber(enterValidNumber("\nNew Department Phone #: "))
            case "4":
                updatingData = False


def removeDepartments(departments):
    listDepartments(departments)
    RemoveName = enterValidString("Please enter the Department you would like to remove: ")

    nameFound = False
    for dept_obj in departments:
        if RemoveName == dept_obj.getDptName():
            print("Name Match! Department Found")
            dpt = dept_obj
            nameFound = True
        
    if nameFound:
        check = enterValidString(f"Are you sure you want to remove {RemoveName}? Y or N: ").lower()
        if check == 'y':
            departments.remove(dpt)
        else:
            print("\nAborting! Returning to previous menu\n")
            time.sleep(1)
    else:
        print("\nNot Found! Returning to previous menu")
        time.sleep(1)



def navigateDepartmentMenu(departments, dpt_dictList):
    file_name = "departments_data.json"

    ViewingDepartments = True
    while ViewingDepartments:
        print("\n1. List All Departments")
        print("2. Add New Department")
        print("3. Update Department")
        print("4. Remove Department")
        print("5. Exit")

        choice = input("\nSelect # option: ")
        choices = ["1", "2", "3", "4", "5"]

        if choice not in choices:
            print("\nPlease choose from the following options")
            continue

        match choice:
            case "1":
                listDepartments(departments)
            case "2":
                addDepartments(departments)
            case "3":
                updateDepartments(departments)
            case "4":
                removeDepartments(departments)
            case "5":
                ViewingDepartments = False

    # Creates a JSON file if none exist
    if not os.path.isfile(file_name):
        with open(file_name, "w") as f:
            pass

    # Serialization and Overriding our Departments JSON
    for dpt in departments:
        appendToDptJSON(file_name, dpt, dpt_dictList)