# bagels.py - Tags: short, game, puzzle.

import random

NUM_DIGITS = 3
MAX_GUSSES = 10


def main():
    print(
        f"""Bagels, a deductive logic game.

I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:     That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct and in the right positon.
    Bagels      No digit is correct.

For example, if the secret number was 986 and your guess was 528, the
clues would be Fermi Pico"""
    )

    # Main game loop.
    while True:
        # Stores the secret number.
        secret_num = get_secret_num()
        print("I have thought up a number.")
        print(f"You have {MAX_GUSSES} guesses to get it.")

        num_guess = 1
        while num_guess <= MAX_GUSSES:
            guess = ""
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{num_guess}")
                guess = input("> ")

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guess += 1

            if guess == secret_num:
                # Gussed right.
                break

            if num_guess > MAX_GUSSES:
                print("You ran out of guesses.")
                print(f"The answer was {secret_num}.")

        # Ask if they want to play again.
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break

    print("Thanks for playing!")


def get_secret_num():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    # Create a list of digits 0 to 9.
    numbers = list("0123456789")
    # Shuffle them into a random order.
    random.shuffle(numbers)

    # Get the first NUM_DIGITS in the list for the secret number.
    secret_num = ""
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
    if guess == secret_num:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit is in the correct place.
            clues.append("Fermi")
        elif guess[i] in secret_num:
            # A correct digit is in the incorrect place.
            clues.append("Pico")
    if len(clues) == 0:
        # There are no correct digits at all.
        return "Bagels"
    else:
        # Sort the clues into alphabetical order so their orginal order doesn't give any information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return " ".join(clues)


if __name__ == "__main__":
    main()
