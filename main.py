import os
import random
from art import logo, vs
from game_data import data

os.system("cls")
print(logo)

def random_account():
    """Select the random profile/account from the data."""
    account = random.choice(data)
    return account

score = 0

celebrity_1 = random_account()
celebrity_2 = random_account()

while True:
    while celebrity_1 == celebrity_2:
        celebrity_2 = random_account()

    print(f"Compare A: {celebrity_1['name']}, a {celebrity_1['description']}, from {celebrity_1['country']}")
    print(vs)
    print(f"Against B: {celebrity_2['name']}, a {celebrity_2['description']}, from {celebrity_2['country']}")

    celebrity_1_followers = celebrity_1['follower_count']
    celebrity_2_followers = celebrity_2['follower_count']

    ask_user = input("Who has more followers? Type 'A' or 'B', or 'q' to quit: ").lower()

    if ask_user == 'q':
        os.system("cls")
        print(logo)
        print(f"Game over! Your final score is {score}.")
        break

    if ask_user == "a":
        if celebrity_1_followers > celebrity_2_followers:
            os.system("cls")
            print(logo)
            print("You guessed it correctly!")
            score += 1
            print(f"Current score: {score}")
            print("------------------------------------------------")
            celebrity_1 = celebrity_2
            celebrity_2 = random_account()
        else:
            os.system("cls")
            print(logo)
            print("You guessed it incorrectly!")
            print(f"Your final score is {score}.")
            input()
            break
    elif ask_user == "b":
        if celebrity_2_followers > celebrity_1_followers:
            os.system("cls")
            print(logo)
            print("You guessed it correctly!")
            score += 1
            print(f"Current score: {score}")
            print("------------------------------------------------")
            celebrity_2 = celebrity_1
            celebrity_1 = random_account()
        else:
            os.system("cls")
            print(logo)
            print("You guessed it incorrectly!")
            print(f"Your final score is {score}.")
            input()
            break
