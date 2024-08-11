import random

import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(art.logo)


def check_score_went_over(listy):
    return sum(listy) > 21


def is_bj(score):
    return score == 21


def add_card(listy):
    card = random.choice(cards)
    if card == 11 and sum(listy) > 21:
        listy.append(1)
    else:
        listy.append(card)


while input("Do you want to play a game of BlackJack? (y/n) ").lower() == "y":
    print("\n" * 20)
    ur_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]

    print(f"Your cards are {str(ur_cards)}, current score is {sum(ur_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

    if is_bj(ur_cards) and not is_bj(computer_cards):
        print("You win! :D")
    elif is_bj(computer_cards):
        print("You lose! 😤")
    else:
        while not check_score_went_over(ur_cards) and input("Type 'y' to get another card, type 'n' to pass: ") == "y":
            add_card(ur_cards)
            print(f"Your cards are {ur_cards}, current score is {sum(ur_cards)}")
            print(f"Computer's first card: {computer_cards[0]}")

        if check_score_went_over(ur_cards):
            print("You went over, You lose! :( ")
        else:
            print(f"Your final hand: {ur_cards}, final score is {sum(ur_cards)}")

            while not check_score_went_over(computer_cards) and sum(computer_cards) <= 16:
                add_card(computer_cards)

            print(f"Computer's final hand: {computer_cards}, final score is {sum(computer_cards)}")

            if check_score_went_over(computer_cards):
                print("Computer went over, You Win! :) ")
            else:
                if sum(computer_cards) > sum(ur_cards):
                    print("You lose! 😤")
                elif sum(computer_cards) == sum(ur_cards):
                    print("Draw 🙃")
                else:
                    print("You win! :D")
