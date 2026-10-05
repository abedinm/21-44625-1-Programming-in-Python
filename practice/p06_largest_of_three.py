"""Practice 06 - comparisons and logical operators.

Task: read three numbers and print the largest one, using if/elif/else
and `and` (not the built-in max()).

Example:
    First: 12
    Second: 45
    Third: 7
    Largest: 45

Run:  uv run python practice/p06_largest_of_three.py
"""


def largest_of_three(a: float, b: float, c: float) -> float:
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def main() -> None:
    a = float(input("First: "))
    b = float(input("Second: "))
    c = float(input("Third: "))
    print(f"Largest: {largest_of_three(a, b, c):g}")


if __name__ == "__main__":
    main()
