def listEmployee(employees_list):
    """
    a function that lists all attributes from each employee object from the employees_list

    Parameters
    ----------
    employees_list : list
        a list of employees objects
    """
    for employee in employees_list:
        print("")
        print(employee.getFirstName(), employee.getLastName(), employee.getEmployeeId(
        ), employee.getDateOfEmployment(), employee.getSalary(), employee.getDepartment())
