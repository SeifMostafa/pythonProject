def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def square(x):
    return x * x


def greet(x):
    print(f"Hello,{x}")


def username():
    return input("What is your name? ")


greet(username())
