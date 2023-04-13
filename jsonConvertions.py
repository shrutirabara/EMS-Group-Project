import json
from Employee import Employee

def appendToJSON(fileName, employee, dictList):
    emp_dict = {
        "first name": employee.getFirstName(),
        "last name": employee.getLastName(),
        "id": employee.getEmployeeId(),
        "doe": employee.getDateOfEmployment(),
        "salary": employee.getSalary(),
        "department": employee.getDepartment()
         }
    
    dictList.append(emp_dict)

    json_obj = json.dumps(dictList)

    with open(fileName, "w") as f:
        f.write(json_obj)

def loadJSONObjects(empl_list, emp_dictList, file_name):
    """
    a function that opens a JSON file and loads it into a list, populating a list with dictionaries
    each dictionary is a representation of a Employee Class Object
    we repopulate employees_list by recreating class objects in memory and appending to the list
    ...

    Parameters
    ----------
    emp_list : str
        an empty list of Employee objects, which we will repopulate
    emp_dictList : str
        a list of dictionaries, which we will load our JSON file array into
    file_name : str
        a JSON file name 
    """
    with open(file_name, "r") as f:
        emp_dictList = json.load(f)

    for emp in emp_dictList:
        recreateClassObj = Employee(
            emp["first name"],
            emp["last name"],
            emp["id"], emp["doe"],
            emp["salary"],
            emp["department"]
            )
        # append employee object to empl_list
        empl_list.append(recreateClassObj)