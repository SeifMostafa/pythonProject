def format_name(first_name, last_name):
    return f"{first_name.title()} {last_name.title()}"


print(format_name(input("Your first name? "), input("Your last name? ")))
