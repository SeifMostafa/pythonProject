from art import logo, vs
from game_data import data
import random

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"



print(logo)
a_acc = random.choice(data)
score = 0
while True:
    b_acc = a_acc
    a_acc = random.choice(data)

    if a_acc == b_acc:
        a_acc = random.choice(data)

    print(f"Compare A: {format_data(a_acc)}")
    print(vs)
    print(f"Against B: {format_data(b_acc)}")
    if check_answer(input("Who has more followers? Type 'A' or 'B':").lower(),a_acc["follower_count"], b_acc["follower_count"]):
        score +=1
    else:
        break


print(f"Sorry, that's wrong. Final score: {score}")