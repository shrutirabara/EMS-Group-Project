class InvalidStringException(Exception):
    pass


def enterValidString(message):
    """
    a function that asks an user for a valid string that is alphabetic only,
    will handle errors and keep prompting until valid

    Parameters
    ----------
    message : str
        a message to prompt the user for anything 
    """

    StringisInvalid = True
    res = ""
    while StringisInvalid:
        try:
            res = input(message)

            if all(x.isalpha() or x.isspace() for x in res):
                StringisInvalid = False
            else:
                print("Bad entry detected!")
                raise InvalidStringException

        except InvalidStringException:
            print("Please enter letters only")
    return res


def enterValidNumber(message):
    """
    a function that asks an user for a valid string that is numeric only,
    will handle errors and keep prompting until valid

    Parameters
    ----------
    message : str
        a message to prompt the user for anything 
    """

    StringisInvalid = True
    res = ""
    while StringisInvalid:
        try:
            res = input(message)

            if res.isnumeric():
                StringisInvalid = False
            else:
                print("Bad entry detected!")
                raise InvalidStringException

        except InvalidStringException:
            print("Please enter numbers only")
    return res
