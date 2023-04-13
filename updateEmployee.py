from errorHandling import enterValidNumber, enterValidString

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
