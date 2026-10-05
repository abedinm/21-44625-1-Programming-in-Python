"""Practice 01 - input, output and variables.

Task: ask for the user's name and birth year, then greet them and say
how old they turn this year.

Example:
    Name: Sam
    Birth year: 2001
    Hello, Sam! You turn 25 in 2026.

Run:  uv run python practice/p01_greeting.py
"""

from datetime import date


def age_this_year(birth_year: int, current_year: int) -> int:
    return current_year - birth_year


def main() -> None:
    name = input("Name: ").strip()
    birth_year = int(input("Birth year: "))
    year = date.today().year
    print(f"Hello, {name}! You turn {age_this_year(birth_year, year)} in {year}.")


if __name__ == "__main__":
    main()
