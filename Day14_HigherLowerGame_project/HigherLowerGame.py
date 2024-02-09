import os
from HigherLowerArt import logo,vs
from HigherLowerData import data
import random

#Pick random accounts
def generate_random_account():
    """Get random account from given input data."""
    return random.choice(data)

#Format data
def format_account_data(account):
    """Format account details in printable format."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"Celebrity / Institution: {name}, a {description}, from {country}"

def compare_followers_data(user_guess, account_a_followers, account_b_followers):
    """Compare account followers."""
    if account_a_followers > account_b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

def high_lower_game():
    # Print logo
    print(logo)
    score = 0
    should_continue = True
    account_b = generate_random_account()

    while should_continue:
        account_a = account_b
        account_b = generate_random_account()

        while account_a == account_b:
            account_b = generate_random_account()

        print(f"Compare A: {format_account_data(account_a)}")
        print(vs)
        print(f"Against B: {format_account_data(account_b)}")

        #Gather user guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        #Compare account followers
        is_correct = compare_followers_data(guess,a_follower_count, b_follower_count)

        os.system('cls')
        # Get score
        if is_correct:
            score+=1
            print(f"You're right! Current score -> {score}")
        else:
            should_continue = False
            print(f"You're wrong! Final score -> {score}")

high_lower_game()