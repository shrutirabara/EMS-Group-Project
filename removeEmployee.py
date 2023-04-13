from errorHandling import enterValidNumber
from listAllEmployees import listEmployee
def removeEmployee(employees_list):
    
    while True:
        try:
            RemoveID = enterValidNumber("Please enter the Employee ID you would like to remove: ")
            check = input("Are you sure you want to remove employee? Y or N: ").lower()
            if check == "y":
                for employee in employees_list:
                    if RemoveID == employee.getEmployeeId():
                        employees_list.remove(employee)
                        
                        print("Successfully deleted")
                        listEmployee(employees_list)
                        again = input("Would you like to continue? Y or N: ").lower()
                        if again == "y":
                            continue
                        elif again == "n":
                            break
                        else:
                            print("That is not a valid answer")
                            continue
                break  
            elif check == "n":
                continue
            else:
                print("That is not a valid answer")
                continue
        except ValueError:
            print("that is not a valid ID")
            continue