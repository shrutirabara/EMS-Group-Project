EmployeeID = [23, 12, 45, 32, 14]
#def removeEmployee(employees_list):
    
while True:
    try:
        RemoveID = int(input("Please enter the Employee ID you would like to remove: "))
        check = input("Are you sure you want to remove this employee? Y or N: ").lower()
        if check == "y":
            if RemoveID in EmployeeID:
                
                '''
                Employees = json.loads(open('employee_data.json').read())
                try:
                    Employees.pop(RemoveID)
                    json.dump(Employees, open('employee_data.json', 'w'))
                except error:
                    print("Employee not found")
                '''
                
                EmployeeID.remove(RemoveID)
                #NewList = (int for int in EmployeeID if int != RemoveID)
                print("Successfully deleted")
                #print(list(NewList))
                print(EmployeeID)
        elif check == "n":
            again = input("Would you like to continue? Y or N: ").lower()
            if again == "y":
                continue
            elif again == "n":
                break
            else:
                print("That is not a valid answer")
                continue
        else:
            print("That is not a valid ID")
            continue
    except ValueError:
        print("that is not a valid ID")
        continue
