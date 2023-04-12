EmployeeID = [23, 12, 45, 32, 14]
def removeEmployee(employees_list):
    
    while True:
        try:
            RemoveID = int(input("Please enter the Employee ID you would like to remove: "))
            check = input("Are you sure you want to remove this employee? Y or N: ").lower()
            if check == "y":
                if RemoveID in EmployeeID:
                    #EmployeeID.remove(RemoveID)
                    NewList = (int for int in EmployeeID if int != RemoveID)
                    #Delete from list
                    print("Successfully deleted")
                    print(list(NewList))
            elif check == "n":
                continue
            else:
                print("That is not a valid answer")
                continue
        except ValueError:
            print("that is not a valid ID")
            continue