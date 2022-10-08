def AddChar(string, character):
    string += character
    return string


def toInt(string):
    return float(string)


def clearString():
    return ""


def delete(string):
    length = len(string)
    if length > 0:
        return string[:-1]
    else:
        return ""


def add(number1, number2):
    return number1+number2


def subtract(number1, number2):
    return number1-number2


def multiply(number1, number2):
    return number1*number2


def devide(number1, number2):
    return number1/number2
