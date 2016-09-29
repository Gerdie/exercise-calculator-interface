def add(list):
    sum = 0
    for num in list:
        sum += num
    return sum

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def square(num1):
    return num1 * num1

def cube(num1):
    return num1 * num1 * num1

def power(num1, num2):
    return num1 ** num2
    """
    base = float(num1)
    if num2 == 0:
        return 1
    elif num2 < 0:
        num1 = float(1/num1)
        num2 = abs(num2)
    for i in range(num2 - 1):
        num1 *= base
    return num1
    """

def mod(num1, num2):
    return num1 % num2
