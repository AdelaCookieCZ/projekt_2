"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Adela Michl
email: kolackova.adela@gmail.com
"""

import random
import time

def create_secret_number() -> str:
    """
    The function generates 4-digits number that does not start with 0 and the digits are unique.
    """
    first_digit = random.choice('123456789')
    remaining_digits = random.sample('0123456789'.replace(first_digit, ''), 3)
    return first_digit + ''.join(remaining_digits)


def calculate_bulls_cows(secret: str, guess: str) -> tuple:
    """
    The function calculates bulls and cows for the secret and the guess.

    Arguments: 
            secret - secret number that is randomly generated
            guess - guessed number from player
            
    Returns:
        tuple(bulls, cows)
    """
    bulls = sum(s == g for s,g in zip(secret, guess))
    cows = len(set(secret) & set(guess)) - bulls
    return bulls, cows


def bulls_and_cows() -> None:
    """
    The function plays the game Bulls and Cows with player. 
    The game generates secret number with unique digits and the player guesses the number. 
    The feedback is provided, if the players guesses the number and the position, it counts bulls, 
    if only the number is correct, it counts cows. The game is finished when the secret number is guessed.
    The function validates user's input, counts the attempts and calculates the length of the game.

    Returns:
        None
    """
    print("""
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
""")
    secret_number = create_secret_number()
    attempts = 0
    start_time = time.time()

    while True:
        player_guess = input("Enter a number: ")

        if len(player_guess) != 4 or len(set(player_guess)) != 4 or not \
            player_guess.isdigit() or player_guess[0] == '0':
            print("Please enter valid 4-digit number that does not start with 0 and the digits are unique.")
            continue

        attempts += 1
        bulls, cows = calculate_bulls_cows(secret_number, player_guess)

        if bulls == 4:
            end_time = time.time()
            total_time = end_time - start_time
            print(f"Correct, you've guessed the right number in {attempts} guess(es)!\nThat's amazing!")
            print(f"It took you {total_time:.2f} seconds.")
            break
        else:
            print(f'{bulls} bulls, {cows} cows')


if __name__ == "__main__":
    bulls_and_cows()
