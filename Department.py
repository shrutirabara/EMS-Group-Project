class Department:
    """
    A class used to represent a Department

    Private Attributes
    ----------
    __name : str
        a string that represents the name of a department
    __dptBudget : float
        a float that represents department budget
    __dptNumber : int
        an int that represents the department phone number
    """
    # Instance Data Members

    def __init__(self, name, budget, phone):
        self.__dptName = name
        self.__dptBudget = budget
        self.__dptNumber = phone

    # Getter Methods

    def getDptName(self):
        return self.__dptName

    def getDptBudget(self):
        return self.__dptBudget

    def getDptNumber(self):
        return self.__dptNumber

    # Setter Methods

    def setDptName(self, nInput):
        self.__dptName = nInput

    def setDptBudget(self, bInput):
        self.__dptBudget = bInput

    def setDptNumber(self, pInput):
        self.__dptNumber = pInput

