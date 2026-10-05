"""Practice 10 - while loops and random numbers.

Task: the computer picks a secret number from 1 to 100. The player keeps
guessing; after each guess say "Go higher" or "Go lower". When they get
it, say how many tries it took. Ignore input that isn't a whole number.

Example:
    I'm thinking of a number from 1 to 100.
    Your guess: 50
    Go lower.
    Your guess: 25
    Go higher.
    Your guess: 37
    Correct! You got it in 3 tries.

Run:  uv run python practice/p10_guess_the_number.py
"""

import random


def check_guess(guess: int, secret: int) -> str:
    if guess < secret:
        return "higher"
    elif guess > secret:
        return "lower"
    else:
        return "correct"


def main() -> None:
    secret = random.randint(1, 100)
    tries = 0
    print("I'm thinking of a number from 1 to 100.")

    while True:
        try:
            text = input("Your guess: ").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\nThe number was {secret}.")
            return

        if not text.isdigit():
            print("Please type a whole number.")
            continue

        tries += 1
        result = check_guess(int(text), secret)
        if result == "correct":
            print(f"Correct! You got it in {tries} {'try' if tries == 1 else 'tries'}.")
            return
        print(f"Go {result}.")


if __name__ == "__main__":
    main()
