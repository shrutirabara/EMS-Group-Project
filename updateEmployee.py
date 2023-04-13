from removeEmployee import EmployeeID


def update_employee():
    print("Enter employee ID to update:")
    emp_id = input()
    emp = EmployeeID(emp_id)
    if emp is not None:
        print("Which attribute do you want to update?")
        print("1. First Name")
        print("2. Last Name")
        print("3. Department")
        print("4. Salary")
        print("5. Date of Employment")
        choice = input()
        if choice == "1":
            print("Enter new first name: ")
            emp.first_name = input()
        elif choice == "2":
            print("Enter new last name: ")
            emp.last_name = input()
        elif choice == "3":
            print("Enter new department: ")
            emp.department = input()
        elif choice == "4":
            print("Enter new salary: ")
            emp.salary = input()
        elif choice == "5":
            print("Enter new date of employment: ")
            emp.date_of_employment = input()
        else:
            print("Invalid choice.")
            return
        print(f"Employee with ID {emp_id} has been updated.")
    else:
        print(f"No employee found with ID {emp_id}.")
