MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def validate_enough_resources(ingredients):
    return (resources["water"] - ingredients["water"] >= 0 and
            resources["milk"] - ingredients["milk"] >= 0 and
            resources["coffee"] - ingredients["coffee"] >= 0)


def process_coins(cost):
    print("Please insert coins.")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickels = int(input("How many nickels?"))
    pennies = int(input("How many pennies?"))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    if total >= cost:
        print(f"Here is {total - cost} in change.")
        print("Here is your espresso ☕️. Enjoy!")
        global money
        money += cost
    else:
        print("Sorry that's not enough money. Money refunded.")


money = 0
user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
while user_choice != "off":
    if user_choice == "espresso" and validate_enough_resources(MENU["espresso"]["ingredients"]):
        process_coins(MENU["espresso"]["cost"])
    elif user_choice == "latte" and validate_enough_resources(MENU["latte"]["ingredients"]):
        process_coins(MENU["latte"]["cost"])
    elif user_choice == "cappuccino" and validate_enough_resources(MENU["cappuccino"]["ingredients"]):
        process_coins(MENU["cappuccino"]["cost"])
    elif user_choice == "report":
        print(resources)
        print("Money: $", money)
    else:
        print("unkown command/drink for our program.. shutting down .. ")
        break
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
