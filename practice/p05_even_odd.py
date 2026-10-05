"""Practice 05 - if/else with numbers.

Task: read a whole number and say whether it is even or odd, and
whether it is positive, negative or zero.

Example:
    Whole number: -7
    -7 is odd and negative.

Run:  uv run python practice/p05_even_odd.py
"""


def parity(number: int) -> str:
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


def sign(number: int) -> str:
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"


def main() -> None:
    number = int(input("Whole number: "))
    print(f"{number} is {parity(number)} and {sign(number)}.")


if __name__ == "__main__":
    main()
