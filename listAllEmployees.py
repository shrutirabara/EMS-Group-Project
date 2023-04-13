def listEmployee(employees_list):
    for employee in employees_list:
        print("")
        print(employee.getFirstName(), employee.getLastName(), employee.getEmployeeId(), employee.getDateOfEmployment(), employee.getSalary(), employee.getDepartment())
