import json
from Employee import Employee
from Department import Department


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


def loadJSONEmpObjects(file_name):
    """
    a function that opens a JSON file and loads it into a list, populating a list with dictionaries
    each dictionary is a representation of a Employee Class Object
    we repopulate employees_list by recreating class objects in memory and appending to the list

    Parameters
    ----------
    file_name : str
        a JSON file name 
    
    Returns
    -------
    departments : list
        a populated list of Employee objects
    emp_dictList : list
        a list of dictionaries, which we will load our JSON file array into
    """
    empl_list, emp_dictList = [], []

    with open(file_name, "r") as f:
        emp_dictList = json.load(f)

    for emp in emp_dictList:
        recreateClassObj = Employee(
            emp["first name"],
            emp["last name"],
            emp["id"],
            emp["doe"],
            emp["salary"],
            emp["department"]
        )
        # append employee object to empl_list
        empl_list.append(recreateClassObj)

    return (empl_list, emp_dictList)


def appendToDptJSON(fileName, dpt, dpt_dictList):
    dpt_dict = {
        "name": dpt.getDptName(),
        "budget": dpt.getDptBudget(),
        "phone": dpt.getDptNumber()
    }

    dpt_dictList.append(dpt_dict)

    json_obj = json.dumps(dpt_dictList)

    with open(fileName, "w") as f:
        f.write(json_obj)

def loadJSONDptObjects(file_name):
    """
    a function that opens a Department JSON file and loads it into a list, populating a list with dictionaries
    each dictionary is a representation of a Department Class Object
    we repopulate dpt_list by recreating class objects in memory and appending to the list

    Parameters
    ----------
    file_name : str
        a Department JSON file name

    Returns
    -------
    departments : list
        a populated list of Department objects
    emp_dictList : list
        a list of dictionaries, which we will load our JSON file array into

    """
    departments, dpt_dictList = [], []

    with open(file_name, "r") as f:
        dpt_dictList = json.load(f)

    for dpt in dpt_dictList:
        recreateClassObj = Department(
            dpt["name"],
            dpt["budget"],
            dpt["phone"]
        )
        # append department object to departments
        departments.append(recreateClassObj)
    
    return (departments, dpt_dictList)
