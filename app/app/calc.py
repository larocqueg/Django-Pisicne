"""
Calculator functions
"""


def add(x, y):
    """Add numbers and return result"""
    return x + y


def subtract(x, y):
    """Subtract numbers and return result"""
    return x - y


def multiply(x, y):
    """Multiply numbers and return result"""
    return x * y


def divide(x, y):
    """Divide numbers and return result"""
    if (y != 0):
        return x / y
    print("Dividing by 0 is impossible!\n")
    return 0
