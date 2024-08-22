def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y



def calculator(operator):
    x = int(input("enter first number "))
    y = int(input("enter second number "))
    return operator(x, y)


def greet(x):
    print(f"Hello,{x}! Welcome to our calculator!")
    op = input("choose operator: (add/sub/multiply/divide/square) or off for shutdown ")
    while op != "off":
        if op == "add":
            print(calculator(add))
        elif op == "subtract":
            print(calculator(subtract))
        elif op == "multiply":
            print(calculator(multiply))
        elif op == "divide":
            print(calculator(divide))
        else:
            print("invalid operator")

        op = input("another operation ? "
                   "choose operator: (add/sub/multiply/divide) or off for shutdown ")


def username():
    return input("What is your name? ")


greet(username())
